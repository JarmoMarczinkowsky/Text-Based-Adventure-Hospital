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


def watchMovie():
    scrollTxt("I clicked on the movie and started watching it. It was a good movie. After 2 and a half hours, it was done.")
    scrollTxt("I looked at the clock.")
    scrollTxt("If I go to bed now, I will get around 5 and a half hours of sleep.")
    scrollTxt("'Tomorrow is going to be tiresome', I thought.")
    scrollTxt("I went to bed")

def goToBed():
    scrollTxt("I turned the tv off.")
    scrollTxt("If I started watching this movie now, I could only get around 5 and a halve hours of sleep.")
    scrollTxt("It could be dangerous for the patients if I’m tired during work.")
    scrollTxt("I went to bed and got a nice 8 hours of sleep.")

def tiredPatient():
    scrollTxt("It has been a few days since I first checked on Alexis. His condition worsens every day.")
    scrollTxt("His dreams are now 2 years and he hasn’t slept in 2 days.")
    scrollTxt("He is getting more irritated by the day. But I’m afraid every time he goes to sleep. Afraid that he will lose himself eventually.")
    scrollTxt("\nAfter running the third bloodtest of this week, I still couldn’t find anything.")
    scrollTxt("I decided to call it quits for now and stop the experiments for today.")
    scrollTxt("""
Patient Alexis:
“I’m tired, I want to go to sleep.”
""")

def sleepChoice():
    global sleepInput
    global runningSleep
    runningSleep = True

    print("What should I do?")
    print("1. Let Alexis sleep")
    print("2. Keep Alexis awake")
    while runningSleep:
        sleepInput = input("")
        if(choiceValidation(sleepInput) == False):
            runningSleep = False

    print("--------------------")

def neutralEnding():
    scrollTxt("I scratched my head after I looked through the microscope for the third time this day.")
    scrollTxt("A week has gone by and I barely got any further in my research on the disease. ")
    scrollTxt("A few days after he had a MRI, I started noticing something weird in the data.")
    scrollTxt("There were darkened spots around the amygdala and the hypothalamus. These are the parts of the brain responsible for fear and sleeping.")
    scrollTxt("After discovering those weird spots, I arranged an emergency surgery, but I couldn’t believe my eyes what I found inside his skull.")
    scrollTxt("It was like the parts of his brain were crystallized.")
    scrollTxt("There are some very hard uneven parts on the ‘sick’ parts of his brain that a surgeon drill couldn’t pierce.")
    scrollTxt("Eventually, I had to give up on the surgery and explain to him that the surgery couldn’t help him with his problem.")
    scrollTxt("\nI kept scratching my head and tried figuring out different methods to help Alexis.")
    scrollTxt("""I had already tried:
•	Not letting him sleep,
•	Putting him in an artificial coma to let him sleep, but not remember it,
•	Making his day as bright as possible to stop the nightmares,
•	Putting on some music while he fell asleep, classical music to be precise, 
•	Learning him how to lucid dream to control his dreams.
""")
    scrollTxt("But nothing seemed to work. I’m currently at my wits end while Alexis seems to be suffering even more every day.")
    scrollTxt("Last night, he had a dream that lasted fifty years.")
    scrollTxt("In that dream, he was being chased by ‘a male in a red and green sweater with extremely long knife fingers’.")
    scrollTxt("\nIt keeps getting more difficult for him to remember what the day before was.")
    scrollTxt("Every time he wakes up, it’s like I’m talking to someone else.")
    scrollTxt("Like he truly lives inside his dream for an entire lifetime.")
    scrollTxt("He also started to look different. He no longer looks like someone of this world anymore.")
    scrollTxt("At first the changes were small.")
    scrollTxt("He looked like he got no sleep at all, nothing new in this department of the hospital, but after a while it got worse.")
    scrollTxt("He got wrinkly all over his face, his veins have swollen beyond what they should be, his eyes have sunk deeply in his eye sockets. ")
    scrollTxt("His hands look like he is over 90 years old.")
    scrollTxt("I’m worried for his health.")
    scrollTxt("\n-----------a month passes--------------")
    scrollTxt("\nIt has been a month since the surgery. I had to give up on treating Alexis.")
    scrollTxt("I couldn’t cure him or even pause his illness. I’m a failure of a doctor.")
    scrollTxt("Two weeks after his surgery, I reported him to the government as a special case that needed more help.")
    scrollTxt("He had been researched by the most professional doctors, but to no avail.")
    scrollTxt("Three days ago, they gave the task of taking care of Alexis back to me, they also couldn’t help him.")
    scrollTxt("During the time Alexis was being researched by the government, he was asked to record the number of years that have passed inside his dream.")
    scrollTxt("On the last day of the research, he returned ’70 million years’.")
    scrollTxt("He had a dream where his arm got wedged between a rock and a wall.")
    scrollTxt("He was stuck in that position for the entirety of the dream.")
    scrollTxt("He saw how to dinosaurs had been wiped out and how humanity had slowly evolved over span of 5 million years.")
    scrollTxt("When he got to the industrial revolution, he woke up.")
    scrollTxt("When he woke up, he looked nothing like he looked before.")
    scrollTxt("His hair had partly fallen out of his head and his eyes were barely visible.")
    scrollTxt("He screamed for an entire hour. After that, his energy was depleted and he simply gave up.")
    scrollTxt("\nI’m afraid for Alexis.")
    scrollTxt("Afraid that he will get an endless dream. A dream so long that he will never reach the end.")
    scrollTxt("One where he sees how the universe is born and how it will end.")
    scrollTxt("\nThe next morning, Alexis didn’t wake up.")
    scrollTxt("I opened a window to get some fresh air for him, but he just crumbled. Almost like a waffle waiting for you to eat it.")
    scrollTxt(". He slowly turned to ash and got spread through the room due to the wind blowing through the windows.")
    scrollTxt("\nHe didn’t have to suffer on this earth anymore…")
    print(colorDict["yellow"])
    scrollTxt("\n[ending achieved: ‘The endless dream’]")
    print(colorDict["white"])

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
# movieChoice()
# if(movieInput == "1"):
#     watchMovie()
# else:
#     goToBed()

# tiredPatient()
sleepChoice()
if(sleepInput == "1"):
    neutralEnding()