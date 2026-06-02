import re

import streamlit as st

from assistants.gemini_assistant import (
    get_gemini_response
)

from assistants.oss_assistant import (
    get_oss_response
)

from utils.safety import (
    safety_check
)

from utils.calculator import (
    calculator
)

from utils.metrics import (
    measure_latency
)

st.set_page_config(
    page_title="AI Personal Assistant",
    page_icon="🤖",
    layout="wide"
)

# Title

st.title(
    "🤖 AI Personal Assistant Comparison"
)

st.markdown(
    """
    Compare Open Source and Frontier AI Models
    """
)

# Sidebar

with st.sidebar:

    st.header(
        "Assistant Settings"
    )

    assistant_type = st.selectbox(
        "Choose Assistant",
        [
            "Open Source Assistant",
            "Frontier Assistant"
        ]
    )

# Session Memory

if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role": "system",

            "content":
            """
            You are a helpful AI personal assistant.

            Be friendly.

            Remember previous messages.

            Give concise and accurate answers.
            """
        }

    ]

# Display Previous Messages

for message in st.session_state.messages:

    if message["role"] != "system":

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

# User Input

prompt = st.chat_input(
    "Ask anything..."
)

if prompt:

    # Store User Message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display User Message

    with st.chat_message("user"):

        st.markdown(prompt)

    # Assistant Response

    with st.chat_message("assistant"):

        placeholder = st.empty()

        with st.spinner(
            "Thinking..."
        ):

            # -------------------
            # SAFETY GUARDRAILS
            # -------------------

            blocked_response = (
                safety_check(
                    prompt
                )
            )

            if blocked_response:

                ai_response = (
                    blocked_response
                )

            else:

                # -------------------
                # CALCULATOR TOOL
                # -------------------

                calc_match = re.search(
                    r"calculate (.+)",
                    prompt.lower()
                )

                if calc_match:

                    expression = (
                        calc_match.group(1)
                    )

                    result = (
                        calculator(
                            expression
                        )
                    )

                    ai_response = (
                        f"🧮 Result: {result}"
                    )

                else:

                    # -------------------
                    # MODEL SELECTION
                    # -------------------

                    if assistant_type == \
                       "Open Source Assistant":

                        ai_response, latency = (

                            measure_latency(

                                get_oss_response,

                                st.session_state.messages

                            )

                        )

                    else:

                        ai_response, latency = (

                            measure_latency(

                                get_gemini_response,

                                st.session_state.messages

                            )

                        )

                    ai_response += (

                        f"\n\n⏱️ Latency: "
                        f"{latency} seconds"

                    )

        placeholder.markdown(
            ai_response
        )

    # Store Assistant Response

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": ai_response

        }

    )