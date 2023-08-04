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
    print(f"{style.RED}dndbot_chat conversation: {conversation}{style.RESET}")

    return render(request, "chat.html", {"conversation": conversation})


def dndbot_clear(request):
    print(f"{style.RED}dndbot_clear clearing session...{style.RESET}")
    request.session.clear()
    return redirect('index')


def dndbot_characters(request):
    return render(request, "characters.html")


def dndbot_create(request):
    campaign = request.session.get("campaign")
    if campaign is None:
        campaign = {
            "numberOfPlayers": 1,
            "minPlayers": 1,
            "maxPlayers": 2,
            "sessionStarted": False
        }
        request.session['campaign'] = campaign
        print(f"{style.RED}dndbot_create new campaign: {campaign}{style.RESET}")
    else:
        print(f"{style.RED}dndbot_create existing campaign: {campaign}{style.RESET}")
    return render(request, "create.html", {"campaign": campaign})

def dndbot_generate(request):
    campaign = request.session.get("campaign")
    campaign["sessionStarted"] = True
    request.session['campaign'] = campaign
    print(f"{style.RED}dndbot_generate campaign: {campaign}{style.RESET}")
    return redirect('dndbot_chat')
