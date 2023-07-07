import os
import openai

from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv

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

def dndbot_view(request):
    conversation = request.session.get("conversation", [])
    print(f"{style.RED}conversation: {conversation}{style.RESET}")

    if request.method == "POST":
        user_input = request.POST.get("user_input")

        # define prompts
        prompts = []

        # append user input to conversation
        if user_input:
            conversation.append({"role": "user", "content": user_input})

        # append conversation messages to prompts
        prompts.extend(conversation)

        # setup and invoke GPT model
        print(f"{style.GREEN}messages sent: {prompts}{style.RESET}") 
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompts
        )

        # extract replies from the response
        print(f"{style.BLUE}response received: {response}{style.RESET}") 
        replies = [message["message"]["content"] for message in response["choices"] if message["message"]["role"] == "assistant"]

        # append replies to the conversation
        for reply in replies:
            conversation.append({"role": "assistant", "content": reply})

        # update the conversation in the session
        request.session["conversation"] = conversation

        return render(request, "chat.html", {"user_input": user_input, "bot_replies": replies, "conversation": conversation})
    else:
        print(f"{style.RED}clearing session...{style.RESET}")
        request.session.clear()
        return render(request, "chat.html", {"conversation": conversation})

def index(request):
    return HttpResponse("Hello, world.")
