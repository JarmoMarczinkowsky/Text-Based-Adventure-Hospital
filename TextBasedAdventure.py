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
       time.sleep(0.015)
    input("")

def introduction():
    scrollTxt("Dr Judy:\n“Dr Leskinen… Dr Leskinen!”")
    scrollTxt("I saw Judy sprinting through the hallway towards me.")
    scrollTxt("Dr Leskinen:\n“Another request to watch one of your patients, Dr Judy?”")
    scrollTxt("Dr Judy seems to be out of breath.")
    scrollTxt("Dr Judy (panting):\n“Yes… I need to be in the ER as soon as possible … could you check up on patient Alexis?")
    scrollTxt("He is in room FG-8, here is his report.”")
    scrollTxt("She pushes the papers in my hands before I could answer and sprints off to the emergency room.")
    scrollTxt(f"I stood there, baffled.  ‘Just another {nowTime.strftime('%A')} in this hospital’, I thought. ")
    scrollTxt(f"I looked at my watch. It’s {nowTime.strftime('%H')}'o clock, time for my well deserved break.")
    scrollTxt("I walk towards the breakroom and sit down.")
    scrollTxt("After looking around for a bit, I decided that I’m bored.")

#inputvalidation
def choiceValidation(userChoice):
    if(str(userChoice).isnumeric()):
        if(int(userChoice) > 0 and int(userChoice) < 3):
            return False
        else:
            print("Please enter 1 or 2")
            return True
    else:
        print("Please enter a valid number:")
        return True

def firstChoice():
    global boredomInput
    global runningFirstChoice
    runningFirstChoice = True

    print("What to do?")
    print("1. Read the rapport")
    print("2. Microwave a banana")
    
    while runningFirstChoice:
        boredomInput = input("")
        if(choiceValidation(boredomInput) == False):
            runningFirstChoice = False

    print("---------------------")


def readRapport():
    scrollTxt("I lean forward and grab the report I put on the table.")
    scrollTxt("It’s a short and to the point report about patient Alexis.")
    scrollTxt(f"""-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Name: Alexis 
Birthday: 13 – 8 – 1998
Sex: Male

Patient number: FE-40536
Married: No
Allergies: Peanuts
 
Hospitalized since: {nowTime.strftime('%B')} {nowTime.strftime('%d')} 
Reason for stay:
Patient describes that he has ‘long dreams’. He claims that his dreams seem to get longer every time he sleeps. 
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
""")
    scrollTxt("""Dr. Leskinen:
“Long dreams, huh. Just because I’m a neurologist it doesn’t mean that I can fix every mental problem everyone has.”
""")
    scrollTxt("I looked at the clock, breaktime was almost over. ")
    scrollTxt("‘Time for me to interview patient Alexis’, I thought.")

def microwaveBanana():
    scrollTxt("I’m so bored that I have decided to do a little science experiment.")
    scrollTxt("I leaned forward and tried to grab a banana from the breakroom fruit bowl.")
    scrollTxt("A few bananas are green and slimy.")
    scrollTxt("‘How long have they been in this bowl?’, I thought.")
    scrollTxt("I grabbed the only banana that didn’t look green and slimy.")
    scrollTxt("I walk towards the microwave, put the banana in and set the timer to 40 seconds.")
    scrollTxt("I press the start button.")
    scrollTxt("I listen to the loud humming the microwave creates.")
    scrollTxt("10 seconds pass.")
    scrollTxt("Suddenly a bright flash appears from the microwave.")
    scrollTxt("Out of reaction, I pull the door open to prevent the microwave from catching fire.")
    scrollTxt("I try to look for the abomination that is supposed to be my banana.")
    scrollTxt("""
Dr. Leskinen:
“What in the goddamn…”
""")
    scrollTxt("The banana is gone. There are no traces of the banana nor the reason there was a flash left.")
    scrollTxt("I have decided to quickly leave this room.")
    scrollTxt("I walk past the table with the fruit bowl on it. There seems to be one green, slimy banana more than there was when I entered this room.")
    scrollTxt("I quickly walk out of the room while thinking about the banana.")

def talkWithPatient():
    scrollTxt("I walk through the hallways and quickly arrive at room FG-8.")
    scrollTxt("I see a patient that looks like the picture that was on the frontpage of the report.")
    scrollTxt("""
Patient Alexis: 
“Good afternoon, doctor”
""")
    scrollTxt("""Dr. Leskinen: 
“Good afternoon, Alexis. I’m doctor Leskinen and I stand in for doctor Judy.”
""")

    if(boredomInput == "1"):
        scrollTxt("""Dr. Leskinen:
“I have seen in your report that you seem to be having something you call ‘long dreams’, 
could you explain to me what a ‘long dream’ is?""")

    else:
        scrollTxt("""Dr. Leskinen:
“Could you explain to me what your problem is?”""")

    scrollTxt("""
Patient Alexis: 
“It all started a month ago, I had a dream that felt like it lasted half a day. 
I thought nothing of it when I woke up, but my dream was longer the next night. 
Instead of a dream that felt like it lasted half a day, it felt like it lasted 15 hours. 
After that, my dreams seemed to get longer every night.”
""")
    scrollTxt("""Dr. Leskinen:
Right...""")
    scrollTxt("""
Dr. Leskinen:
“And how long are your dreams now?”
""")
    scrollTxt("""Patient Alexis: 
“Last night it felt like I got trapped inside my dream for half a year.”
""")
    scrollTxt("""Dr. Leskinen: 
“So every time you wake up it feels like your dream had lasted a while?”
""")
    scrollTxt("""Patient Alexis:
“No doctor, It is inside the dream that I feel time drag on. 
In the beginning I wasn’t sure, but with every passing day, the dreams grew longer”
“It wouldn’t even be halve so bad if it isn’t a nightmare I am trapped inside of.”
“Last night I was trapped in a never ending maze for a day. 
The day before that I was trapped inside a dream where I was swimming in the middle of the ocean for a long time.”
""")
    scrollTxt("I could barely keep myself under control. It took a lot of restraint to not grin at this absurd statement.")
    scrollTxt("""
Patient Alexis: 
“I can barely remember the day before, when I wake up. This has become a problem that impairs my daily life.”
""")
    scrollTxt("I couldn’t believe him, I thought he was making fun of me. Or in the worst case scenario: has an underlying mental problem.")
    scrollTxt("I have decided to hook him up to a machine that graphs your brain activity when you sleep.")
    scrollTxt("Around 40 minutes after he fell asleep, he began shaking and his graph began creating extraordinary high lines.")
    scrollTxt("I decided to wake him up. I grabbed his shoulders and started shaking them.")
    scrollTxt("""
Dr. Leskinen:
“Hey, Alexis, wake up!”
""")
    scrollTxt("Alexis opened his eyes.")
    scrollTxt("""
Patient Alexis:
“Where am I?”
""")
    scrollTxt("He looked at me like he was seeing a stranger.")
    scrollTxt("""
Dr. Leskinen:
“You’ve been admitted to this hospital a few days ago, try to remember.”
""")
    scrollTxt("He slowly started to remember why he was here.")
    scrollTxt("""
Alexis:
“…”
“I had a terrifying dream that lasted 200 days.” 
""")
    scrollTxt("After this I experimented with him a few times more.")
    scrollTxt("Every time he entered REM-sleep, he started shaking uncontrollably")
    scrollTxt("The dream always happens in that split-second he starts shaking.")
    scrollTxt("Puzzled, I went home.")

def atHome():
    scrollTxt("After I left the hospital, because my shift was over. I decided to make a quick stop at a fastfood restaurant before going home.")
    scrollTxt("I was thinking about Alexis’ case while I was eating my burger.")
    scrollTxt("‘It shouldn’t be possible’, I thought")
    scrollTxt("I decided to check the internet for this case. The only thing close to my problem was a horror manga.")
    scrollTxt("Defeated, I closed the laptop.")
    scrollTxt("\n‘Let’s just unwind a bit before I go to sleep’\n")
    scrollTxt("I turned the tv on and scrolled through Netflix.")
    scrollTxt("There was nothing interesting so I started browsing on my phone.")
    scrollTxt("After a while I noticed that the time went by quickly and it was almost time for bed.")
    scrollTxt("Suddenly Netflix recommended me a movie that seemed interesting.")
    scrollTxt("“Along with the Gods: the worlds between”")

def movieChoice():
    global movieInput
    global runningMovie
    runningMovie = True

    print("What should I do?")
    print("1. Watch a movie")
    print("2. Go to bed early")
    while runningMovie:
        movieInput = input("")
        if(choiceValidation(movieInput) == False):
            runningMovie = False
        
    print("------------------")

    
#---------------------------------------------------------------------------------------------

system("cls")
# introduction()
# firstChoice()

# if(boredomInput == "1"):
#     readRapport()
# elif(boredomInput == "2"):
#     microwaveBanana()

# talkWithPatient()
# atHome()
movieChoice()