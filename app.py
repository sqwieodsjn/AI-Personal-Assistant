import streamlit as st

from assistants.gemini_assistant import (
    get_gemini_response
)

from assistants.oss_assistant import (
    get_oss_response
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

    # Save User Message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show User Message

    with st.chat_message("user"):

        st.markdown(prompt)

    # Generate Response

    with st.chat_message("assistant"):

        placeholder = st.empty()

        with st.spinner(
            "Thinking..."
        ):

            if assistant_type == \
               "Open Source Assistant":

                ai_response = (
                    get_oss_response(
                        st.session_state.messages
                    )
                )

            else:

                ai_response = (
                    get_gemini_response(
                        st.session_state.messages
                    )
                )

        placeholder.markdown(
            ai_response
        )

    # Save Assistant Response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )