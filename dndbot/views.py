import os

from django.shortcuts import render
from django.shortcuts import redirect

os.system("")


class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'


def index(request):
    return render(request, "index.html")


def dndbot_chat(request):
    conversation = request.session.get("conversation", [])
    print(f"{style.RED}conversation: {conversation}{style.RESET}")

    return render(request, "chat.html", {"conversation": conversation})


def dndbot_clear(request):
    print(f"{style.RED}clearing session...{style.RESET}")
    request.session.clear()
    return redirect('index')


def dndbot_characters(request):
    return render(request, "characters.html")


def dndbot_create(request):
    campaign = request.session.get("campaign", {
        "numberOfPlayers": 1,
        "minPlayers": 1,
        "maxPlayers": 2
    })
    print(f"{style.RED}campaign: {campaign}{style.RESET}")
    return render(request, "create.html", {"campaign": campaign})
