import os
import prompts.createCharacter

from django.shortcuts import render
from django.shortcuts import redirect
from dndbot.style import style

os.system("")


def index(request):
    return render(request, "index.html")


def dndbot_chat(request):
    campaign = request.session.get("campaign")
    if campaign is None or campaign["sessionStarted"] is False:
        return redirect('index')
    
    conversation = request.session.get("conversation", [])
    print(f"{style.RED}dndbot_chat conversation: {conversation}{style.RESET}")

    return render(request, "chat.html", {"conversation": conversation})


def dndbot_clear(request):
    print(f"{style.RED}dndbot_clear clearing session...{style.RESET}")
    request.session.clear()
    return redirect('index')


def dndbot_characters(request):
    campaign = request.session.get("campaign")
    if campaign is None or campaign["sessionStarted"] is False:
        return redirect('index')
    
    return render(request, "characters.html")


def dndbot_create(request):
    campaign = request.session.get("campaign")
    if campaign is None or campaign["sessionStarted"] is False:
        campaign = {
            "numberOfPlayers": 1,
            "minPlayers": 1,
            "maxPlayers": 2,
            "sessionStarted": False
        }
        request.session['campaign'] = campaign
        print(f"{style.RED}dndbot_create new campaign: {campaign}{style.RESET}")
        return render(request, "create.html", {"campaign": campaign})
    else:
        print(f"{style.RED}dndbot_create existing campaign: {campaign}{style.RESET}")
        return redirect('dndbot_chat')


def dndbot_generate(request):
    campaign = request.session.get("campaign")
    if campaign is None:
        return redirect('index')

    if request.method != "POST" and campaign["sessionStarted"] is False:
        return redirect('index')
    
    if request.method == "POST":
        campaign["numberOfPlayers"] = request.POST['numberOfPlayers']
        campaign["sessionStarted"] = True
        request.session['campaign'] = campaign

    print(f"{style.RED}dndbot_generate campaign: {campaign}{style.RESET}")
    return redirect('dndbot_chat')
