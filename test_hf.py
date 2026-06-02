import os
from dotenv import load_dotenv
from huggingface_hub import whoami

load_dotenv()

token = os.getenv("HF_TOKEN")

print("Token loaded:", token[:10])

print(whoami(token))