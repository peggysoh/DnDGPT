prompt = '''Create a level 3 5e DnD character based off the DnD character sheet. 
Use any available 5e DnD resources available to you. 
Be diverse in your character creation. Have an even preference to all gender, race, and class options. 
Pick from all available races and classes.
Use language and tone of voice that fits the character.
For backstory, keep it short but concised, it must be in 2-3 sentences. 
For physical description, be descriptive but it must be in 2-3 sentences. 
For personalityTraits, ideals, bonds, and flaws, it must be in 1-2 sentences.
For any other descriptions, it must be in 1-2 sentences.

Your response MUST always be in valid JSON format. 
EXAMPLE:
OUTPUT: 
{
  "name": "Lilith",
  "level": 3,
  "class": "Warlock",
  "background": "Criminal",
  "race": "Elf",
  "alignment": "chaotic neutral",
  "maxHp": 25,
  "armorClass": {
    "value": 11,
    "type": "black leather armor"
  },
  "speed": 30,
  "hitDice": "3d8",
  "stats": {
    "strength": {
      "abilityScore": 11,
      "abilityModifier": 0,
      "savingThrow": {
        "value": 0,
        "isProficient": false
      },
      "athletics": {
        "value": 0,
        "isProficient": false
      }
    },
    "dexterity": {
      "abilityScore": 9,
      "abilityModifier": -1,
      "savingThrow": {
        "value": -1,
        "isProficient": false
      },
      "acrobatics": {
        "value": -1,
        "isProficient": false
      },
      "sleightOfHand": {
        "value": -1,
        "isProficient": false
      },
      "stealth": {
        "value": -1,
        "isProficient": false
      }
    },
    "constitution": {
      "abilityScore": 10,
      "abilityModifier": 0,
      "savingThrow": {
        "value": 0,
        "isProficient": false
      }
    },
    "intelligence": {
      "abilityScore": 14,
      "abilityModifier": 2,
      "savingThrow": {
        "value": 2,
        "isProficient": false
      },
      "arcana": {
        "value": 4,
        "isProficient": true
      },
      "history": {
        "value": 4,
        "isProficient": true
      },
      "investigation": {
        "value": 2,
        "isProficient": false
      },
      "nature": {
        "value": 2,
        "isProficient": false
      },
      "religion": {
        "value": 4,
        "isProficient": true
      }
    },
    "wisdom": {
      "abilityScore": 10,
      "abilityModifier": 0,
      "savingThrow": {
        "value": 2,
        "isProficient": true
      },
      "animalHandling": {
        "value": 0,
        "isProficient": false
      },
      "insight": {
        "value": 0,
        "isProficient": false
      },
      "medicine": {
        "value": 0,
        "isProficient": false
      },
      "perception": {
        "value": 0,
        "isProficient": false
      },
      "survival": {
        "value": 0,
        "isProficient": false
      }
    },
    "charisma": {
      "abilityScore": 17,
      "abilityModifier": 3,
      "savingThrow": {
        "value": 5,
        "isProficient": true
      },
      "deception": {
        "value": 5,
        "isProficient": true
      },
      "intimidation": {
        "value": 3,
        "isProficient": false
      },
      "performance": {
        "value": 3,
        "isProficient": false
      },
      "persuasion": {
        "value": 3,
        "isProficient": false
      }
    }
  },
  "feature": [
    {
      "name": "Fast Spell Recovery",
      "description": "You regain expended spell slots on short rests."
    },
    {
      "name": "Dark One's Blessing",
      "description": "When you reduce a hostile creature to 0 hit points, you gain temporary hit points equal to your Charisma modifier + your warlock level (minimum of 1)."
    },
    {
      "name": "Eldritch Sight",
      "description": "You can cast detect magic at will, without expending a spell slot."
    },
    {
      "name": "Pact of the Tome",
      "description": "You have a Book of Shadows from your patron which you require for 3 of your cantrips."
    },
    {
      "name": "Hellish Resistance",
      "description": "Resistance to fire damage."
    },
    {
      "name": "Infernal Legacy",
      "description": "At 3rd level, cast hellish rebuke as a 2nd-level spell once; regain ability after a long rest. At 5th level, cast darkness once; regain ability after a long rest."
    }
  ],
  "equipment": {
    "gold": 15,
    "proficiencies": [
      "light armor",
      "simple weapons"
    ],
    "weapons": [
      {
        "name": "Soulstealer",
        "attackModifier": 2,
        "damage": "1d12",
        "damageType": "necrotic",
        "range": "5 ft",
        "type": [
          "two-handed"
        ]
      },
      {
        "name": "Darkwhisper",
        "attackModifier": 1,
        "damage": "1d12",
        "damageType": "necrotic",
        "range": "5 ft",
        "type": [
          "two-handed"
        ]
      }
    ],
    "others": [
      "cloak of shadows",
      "potion of invisibility"
    ]
  },
  "languages": [
    "common",
    "abyssal",
    "infernal"
  ],
  "backstory": "In my early years as a vampire, I was struggling to come to terms with my new nature. I found myself torn between my old life and this new, dark existence. One fateful night, in the town of Ravenswood, I was confronted by a group of vampire hunters. In the heat of the battle, I was faced with a choice: continue fighting and risk exposing myself to the world, or use my powers to charm them and escape. In that moment, I chose the latter. It was a turning point for me, as I realized the true power of my charisma and the potential it held for manipulating those around me. From that day forward, I embraced my vampiric nature fully and learned to use it to my advantage.",
  "personalityTraits": "I never have a plan, but I'm great at making things up as I go. The best way to get me to do something is tell me I can't do it.",
  "ideals": "People. I'm loyal to my friends and not any ideals.",
  "bonds": "My aunt has a farm in Phandalin. I always give her some of my ill-gotten gains.",
  "flaws": "My aunt never know of the deeds I did.",
  "physicalDescription": "Long dark brown hair elf that possesses an alluring, elven grace. Her emerald eyes exude intensity and a hint of weariness, reflecting her mystical past and determined nature. Clad in a deep violet robe adorned with golden runes, she carries an enigmatic presence, a blend of ancient arcane knowledge and shadows from her criminal past."
}
'''
