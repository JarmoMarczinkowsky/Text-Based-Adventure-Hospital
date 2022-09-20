import os
from os import system
import time
from time import sleep
import sys
import random

def scrollTxt(text):
   for char in text:
       sys.stdout.write(char)
       sys.stdout.flush()
       time.sleep(0.035)


colorDict = {
    "black" : "\033[0;30m",
    "purple" : "\033[0;35m",
    "blue" : "\033[0;34m",
    "green" : "\033[0;32m",
    "red" : "\033[0;31m",
    "yellow" : "\033[0;33m",
    "white" : "\033[0;37m"
}

print(colorDict["blue"])

scrollTxt("qwesrdgyjk;.qwertgjkl,;awsfdfhgh")