import os

from dotenv import load_dotenv

from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    token=os.getenv(
        "HF_TOKEN"
    )
)


def get_oss_response(messages):

    response = client.chat_completion(

        model="Qwen/Qwen2.5-7B-Instruct",

        messages=messages,

        max_tokens=200
    )

    return (
        response
        .choices[0]
        .message
        .content
    )