import os
import openai

from dotenv import load_dotenv

# Set OpenAI API Key
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
if openai.api_key is None:
    raise ValueError(
        "OpenAI API Key not set as environnment variable OPENAI_API_KEY")

os.system("")

def chatComplete(prompts):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=prompts
    )
