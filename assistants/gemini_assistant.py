import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def get_gemini_response(messages):

    conversation = ""

    for msg in messages:

        conversation += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    retries = 3

    for attempt in range(retries):

        try:

            response = (
                model.generate_content(
                    conversation
                )
            )

            return response.text

        except Exception as e:

            if "429" in str(e):

                print(
                    "Rate limit hit. Waiting 60 seconds..."
                )

                time.sleep(60)

            else:

                return (
                    f"ERROR: {e}"
                )

    return (
        "ERROR: Maximum retries exceeded"
    )