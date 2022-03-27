import json
from random import random


def loadWord() -> list:
    import os
    if os.path.abspath(".") == "/home/user":
        os.chdir("/workspace/Project1/")
    with open("word.json", "r") as f:
        data = json.load(f)
    return data


def randWord() -> str:
    data = loadWord()
    rand = int(random() * len(data))
    return data[rand]


def findWord(text: str) -> tuple:
    data = loadWord()
    return text in data


def compare(key: str, text: str) -> str:
    result = ""
    for i in range(5):
        if text[i] == key[i]:
            result += f"[rgb(0,255,0)]{text[i]}[/rgb(0,255,0)]"
        elif text[i] in key:
            result += f"[rgb(0,0,255)]{text[i]}[/rgb(0,0,255)]"
        else:
            result += f"[rgb(255,0,0)]{text[i]}[/rgb(255,0,0)]"
    return result
