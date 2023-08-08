import base64
import io
import os
import openai

from dotenv import load_dotenv
from PIL import Image

# Set OpenAI API Key
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
if openai.api_key is None:
    raise ValueError(
        "OpenAI API Key not set as environnment variable OPENAI_API_KEY")

os.system("")

def chatComplete(prompts):
    return openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-16k",
        messages = prompts
    )

def imageCreate(filename, prompt):
    response = openai.Image.create(
        prompt = prompt,
        n = 1,
        size = "512x512",
        response_format = "b64_json"
    )
    imageData = response['data'][0]['b64_json']
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(imageData, "utf-8"))))
    img.save(f'static\images\{filename}', format='JPEG', quality=100, subsampling=0)
