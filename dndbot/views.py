import os
import openai

from django.shortcuts import render
from dotenv import load_dotenv
from django.shortcuts import redirect

# Set OpenAI API Key
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
if openai.api_key is None:
    raise ValueError("OpenAI API Key not set as environnment variable OPENAI_API_KEY")

os.system("")
class style():
  RED = '\033[31m'
  GREEN = '\033[32m'
  BLUE = '\033[34m'
  RESET = '\033[0m'

def index(request):
    return render(request, "index.html")

def dndbot_get(request):
    conversation = request.session.get("conversation", [])
    print(f"{style.RED}conversation: {conversation}{style.RESET}")
    return render(request, "chat.html", {"conversation": conversation})

def dndbot_post(request): 
    conversation = request.session.get("conversation", [])
    print(f"{style.RED}conversation: {conversation}{style.RESET}")

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        print(f"{style.RED}user_input: {user_input}{style.RESET}")

        # define prompts
        prompts = []

        # append user input to conversation
        if user_input:
            conversation.append({"role": "user", "content": user_input})

        # append conversation messages to prompts
        prompts.extend(conversation)

        # setup and invoke GPT model
        #print(f"{style.GREEN}messages sent: {prompts}{style.RESET}") 
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=prompts
        # )
        
        # mock response
        print(f"{style.GREEN}Mock response...{style.RESET}") 
        response = {
            "choices": [
                {
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "content": "Hello! How can I help you today?",
                    "role": "assistant"
                }
                }
            ],
            "created": 1688771423,
            "id": "chatcmpl-7ZoshA7FcBJxCzRpS8vtuAAtJn6H4",
            "model": "gpt-3.5-turbo-0613",
            "object": "chat.completion",
            "usage": {
                "completion_tokens": 9,
                "prompt_tokens": 8,
                "total_tokens": 17
            }
        }

        # extract replies from the response
        print(f"{style.BLUE}response received: {response}{style.RESET}") 
        replies = [message["message"]["content"] for message in response["choices"] if message["message"]["role"] == "assistant"]

        # append replies to the conversation
        for reply in replies:
            conversation.append({"role": "assistant", "content": reply})

        # update the conversation in the session
        request.session["conversation"] = conversation
        return redirect('dndbot_get')
    else:
        print(f"{style.RED}clearing session...{style.RESET}")
        request.session.clear()
        return render(request, "chat.html", {"conversation": conversation})
