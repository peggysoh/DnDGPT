import json
import os
import openai

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import render
from dotenv import load_dotenv
from django.shortcuts import redirect

# Set OpenAI API Key
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
if openai.api_key is None:
    raise ValueError(
        "OpenAI API Key not set as environnment variable OPENAI_API_KEY")

os.system("")


class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "chat_dndbot"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        # get conversation from session
        session_data = await sync_to_async(self.scope["session"].load)()
        conversation = session_data.get("conversation", [])
        print(f"{style.BLUE}session_data: {session_data}{style.RESET}")

        # get user input
        text_data_json = json.loads(text_data)
        userInput = text_data_json["userInput"]
        print(f"{style.RED}userInput: {userInput}{style.RESET}")

        # append user input to conversation
        if userInput:
            conversation.append({"role": "user", "content": userInput})

        # define prompts
        prompts = []
        prompts.extend(conversation)

        # setup and invoke GPT model
        print(f"{style.GREEN}prompts: {prompts}{style.RESET}")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=prompts
        )

        # mock response
        # print(f"{style.GREEN}Mock response...{style.RESET}")
        # response = {
        #     "choices": [
        #         {
        #             "finish_reason": "stop",
        #             "index": 0,
        #             "message": {
        #                 "content": "Hello! How can I help you today?",
        #                 "role": "assistant"
        #             }
        #         }
        #     ],
        #     "created": 1688771423,
        #     "id": "chatcmpl-7ZoshA7FcBJxCzRpS8vtuAAtJn6H4",
        #     "model": "gpt-3.5-turbo-0613",
        #     "object": "chat.completion",
        #     "usage": {
        #         "completion_tokens": 9,
        #         "prompt_tokens": 8,
        #         "total_tokens": 17
        #     }
        # }

        # extract replies from the response
        print(f"{style.GREEN}response: {response}{style.RESET}")
        replies = [message["message"]["content"]
                   for message in response["choices"] if message["message"]["role"] == "assistant"]

        # append replies to the conversation
        for reply in replies:
            conversation.append({"role": "assistant", "content": reply})

        # save session
        session_data["conversation"] = conversation
        self.scope['session'].update(session_data)
        await sync_to_async(self.scope["session"].save)()
        print(f"{style.BLUE}new_session_data: {conversation}{style.RESET}")

        await self.send(text_data=json.dumps({"response": conversation[-1]}))
