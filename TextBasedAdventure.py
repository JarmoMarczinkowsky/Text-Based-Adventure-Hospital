import os
from os import system
import time
from time import sleep
import sys
import random
from turtle import color

def scrollTxt(text, textColor):
    print(textColor, end="")
    for char in text:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(0.035)
    input("")

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

# print(colorDict["green"])

scrollTxt("red text", colorDict["red"])
scrollTxt("white text", colorDict["white"])
scrollTxt("yellow text", colorDict["yellow"])