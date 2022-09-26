import os
from os import system
import time
from time import sleep
import sys
import random
from turtle import color
from datetime import datetime, timedelta

nowTime = datetime.today() - timedelta(days=3)
# print(f"{nowTime.strftime('%B')} {nowTime.day}")

#don't forget: 
#change the '0;' to '1;' for bold text 
colorDict = {
    "black" : "\033[0;30m",
    "purple" : "\033[0;35m",
    "blue" : "\033[0;34m",
    "green" : "\033[0;32m",
    "lightGreen" : "\033[1;32m",
    "red" : "\033[0;31m",
    "yellow" : "\033[0;33m",
    "white" : "\033[0;37m"
}

def scrollTxt(text):
    for char in text:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(0.025)
    input("")

def introduction():
    scrollTxt("Dr Judy: “Dr Leskinen… Dr Leskinen!”")
    scrollTxt("I saw Judy sprinting through the hallway towards me.")
    scrollTxt("Dr Leskinen: “Another request to watch one of your patients, Dr Judy?”")
    scrollTxt("Dr Judy seems to be out of breath.")
    scrollTxt("Dr Judy (panting): “Yes… I need to be in the ER as soon as possible … could you check up on patient Alexis?")
    scrollTxt("He is in room FG-8, here is his report.”")
    scrollTxt("She pushes the papers in my hands before I could answer and sprints off to the emergency room.")
    scrollTxt(f"I stood there, baffled.  ‘Just another {nowTime.strftime('%A')} in this hospital’, I thought. ")
    scrollTxt(f"I looked at my watch. It’s {nowTime.strftime('%H')}'o clock, time for my well deserved break.")
    scrollTxt("I walk towards the breakroom and sit down.")
    scrollTxt("After looking around for a bit, I decided that I’m bored.")

def firstChoice():
    print("What to do?")
    print("1. Read the rapport")
    print("2. Microwave a banana")
    boredomInput = input("")



system("cls")
# introduction()
firstChoice()