import json
import os
import dndbot.openaiprovider as openai_provider

from django.shortcuts import render
from django.shortcuts import redirect
from dndbot.prompts.createCharacter import prompt as createCharacterPrompt
from dndbot.prompts.createCharacterImage import prompt as createCharacterImgPrompt 
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
    
    characters = []
    charactersJson = campaign["characters"]
    for characterJson in charactersJson:
        character = json.loads(characterJson)
        name = "%s_%s" % (character['firstName'], character['lastName'])
        character["imageUrl"] = f'images/characters/{name}.jpg'
        characters.append(character)
    print(f"{style.GREEN}dndbot_characters: {characters}{style.RESET}")
    return render(request, "characters.html", {"characters": characters})


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
        numberOfPlayers = int(request.POST['numberOfPlayers'])
        characters = []
        for i in range(numberOfPlayers):
            prompts = []
            prompts.extend([{"role": "user", "content": createCharacterPrompt}])
            print(f"{style.RED}dndbot_generate creating character...{style.RESET}")
            response = openai_provider.chatComplete(prompts)
            
            replies = [message["message"]["content"]
                    for message in response["choices"] if message["message"]["role"] == "assistant"]

            for reply in replies:
                characters.append(reply)
                try:
                    character = json.loads(reply)
                except json.decoder.JSONDecodeError:
                    print("Invalid JSON")
                    
                if 'physicalDescription' in character and 'firstName' in character and 'lastName' in character:
                    name = "%s_%s" % (character['firstName'], character['lastName'])
                    print(f"{style.RED}dndbot_generate creating character image...{style.RESET}")
                    charImgPrompt = "%s %s" % (createCharacterImgPrompt, character['physicalDescription'] )
                    openai_provider.imageCreate(f'characters/{name}.jpg', charImgPrompt)

        campaign["characters"] = characters
        campaign["numberOfPlayers"] = numberOfPlayers
        campaign["sessionStarted"] = True
        request.session['campaign'] = campaign
        print(f"{style.RED}dndbot_generate character creation done...{style.RESET}")

    return redirect('dndbot_chat')
