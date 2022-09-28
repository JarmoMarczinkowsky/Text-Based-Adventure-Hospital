import os
from os import system
import time
from time import sleep
import sys
import random
from turtle import color
from datetime import datetime, timedelta

threeDaysAgo = datetime.today() - timedelta(days=3)
nowTime = datetime.now()

#Colors that I could color the text with
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
       time.sleep(0.005)
    input("")

def introduction():
    scrollTxt("Dr Judy:\n“Dr Leskinen… Dr Leskinen!”\n")
    scrollTxt("I saw Judy sprinting through the hallway towards me.")
    scrollTxt("\nDr Leskinen:\n“Another request to watch one of your patients, Dr Judy?”\n")
    scrollTxt("Dr Judy seems to be out of breath.")
    scrollTxt("\nDr Judy (panting):\n“Yes… I need to be in the ER as soon as possible … could you check up on patient Alexis?\n")
    scrollTxt("He is in room FG-8, here is his report.”\n")
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
    scrollTxt("I quickly walk out of the room while thinking about the banana.\n")

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
“So every time you wake up it feels like your dream has lasted a while?”
""")
    scrollTxt("""Patient Alexis:
“No doctor, It is inside the dream that I feel time drag on. 
In the beginning I wasn’t sure, but with every passing day, the dreams grew longer.
It wouldn’t even be halve so bad if it isn’t a nightmare I am trapped inside of.
Last night I was trapped in a never ending maze for a day. 
The day before that I was trapped inside a dream where I was swimming in the middle of the ocean for a long time.”
""")
    scrollTxt("I could barely keep myself under control. It took a lot of restraint to not grin at this absurd statement.")
    scrollTxt("""
Patient Alexis: 
“I can barely remember the day before when I wake up. This has become a problem that impairs my daily life.”
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
    scrollTxt("Every time he entered REM-sleep, he started shaking uncontrollably.")
    scrollTxt("The dream always happens in that split-second he starts shaking.")
    scrollTxt("Puzzled, I went home.\n")

def atHome():
    scrollTxt("After that I left the hospital, because my shift was over. I decided to make a quick stop at a fastfood restaurant before going home.")
    scrollTxt("I was thinking about Alexis’ case while I was eating my burger.")
    scrollTxt("‘It shouldn’t be possible’, I thought.")
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
    scrollTxt("I went to bed.\n")

def goToBed():
    scrollTxt("I turned the tv off.")
    scrollTxt("If I started watching this movie now, I could only get around 5 and a halve hours of sleep.")
    scrollTxt("It could be dangerous for the patients if I’m tired during work.")
    scrollTxt("I went to bed and got a nice 8 hours of sleep.\n")

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

def panickedPatientChoice():
    global panicInput
    
    runningPanic = True
    
    print("What should I do?")
    print("1. Leave the room")
    print("2. Calm the patient")
    while runningPanic:
        panicInput = input("")
        if(choiceValidation(panicInput) == False):
            runningPanic = False
    
    print("--------------------")

def calmPatientChoice():
    global calmPatientInput

    runningCalmPatient = True

    print("How should I calm Alexis?")
    print("1. Food")
    print("2. Medicines")
    while runningCalmPatient:
        calmPatientInput = input("")
        if(choiceValidation(calmPatientInput) == False):
            runningCalmPatient = False

    print("--------------------")


#endings
#--------------------------------------------------------------------------------------------------------------

def neutralEnding():
    scrollTxt("--------------------------------------------")
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
•	Putting on some music while he fell asleep. Classical music to be precise, 
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
    scrollTxt("He saw how to dinosaurs had been wiped out and how humanity had slowly evolved.")
    scrollTxt("When he got to the industrial revolution, he woke up.\n")
    scrollTxt("When he woke up, he looked nothing like he looked before.")
    scrollTxt("His hair had partly fallen out of his head and his eyes were barely visible.")
    scrollTxt("He screamed for an entire hour. After that, his energy was depleted and he simply gave up.")
    scrollTxt("\nI’m afraid for Alexis.")
    scrollTxt("Afraid that he will get an endless dream. A dream so long that he will never reach the end.")
    scrollTxt("One where he sees how the universe is born and how it will end.")
    scrollTxt("\nThe next morning, Alexis didn’t wake up.")
    scrollTxt("I opened a window to get some fresh air for him, but he just crumbled. Almost like a waffle waiting for you to eat it.")
    scrollTxt("He slowly turned to ash and got spread through the room due to the wind blowing through the windows.")
    scrollTxt("\nHe didn’t have to suffer on this earth anymore…")
    print(colorDict["yellow"])
    scrollTxt("\n[ending achieved: ‘The endless dream’]\n")
    print(colorDict["white"])

def badEnding():
    scrollTxt("""
Dr. Leskinen:
“I will make another coffee for you, so just stay awake for a little longer.”
""")
    scrollTxt("I walked out of the room before Alexis could reject the idea.")

    if(movieInput == "1"):

        scrollTxt("I scratched my beard before I noticed that I forgot my mask.")
        scrollTxt("It must be because I'm tired. I was up late watching different Netflix series the last few days.")
        scrollTxt("""
Dr. Leskinen:
"I sure hope that whatever Alexis has, it is something that is not transmissible by air."
""")
    scrollTxt("I was walking to the coffee machine when I saw Dr. Judy. ")
    scrollTxt("I hadn’t seen her in days since she was the best doctor on the Emergency Room department.")
    scrollTxt("While I was chatting up with her, I heard a bloodcurdling scream.")
    scrollTxt("I saw a patient run through the hallways with a look like she had seen the grim reaper.")
    scrollTxt("Behind her was Alexis. Trying to match her speed while dragging his left leg behind him.")
    scrollTxt("He ran like an elderly man with a leg that looked like it hurt.")
    scrollTxt("""
Patient Alexis:
“Please… someone… help me…”
""")
    scrollTxt("He sounded tired and sad at the same time.")
    scrollTxt("\nI quickly ran after Alexis and after catching him I guided him back to his room.")
    scrollTxt("""
Dr. Leskinen (angry):
“What do you think you are doing?!”
""")
    scrollTxt("""Patient Alexis:
“I needed to get out of that room, doctor. In my last dream, I was trapped inside this room for over two years. 
When I woke up, I couldn’t distinguish between my dream and reality. 
But when you left the room, I panicked so much that I started running. 
I entered the first open room that I found and in that was a girl that started screaming.”
""")
    scrollTxt("While Alex was getting more calmer in his room, I started looking for the girl that he chased.")
    scrollTxt("After searching around for a bit, I found her in her own hospital room with Judy next to her.")
    scrollTxt("Judy was trying to calm her down, but it didn’t seem to help much.")
    scrollTxt("\nThe girl was screaming about having seen the god of death and that her time was near.")
    scrollTxt("She meant Alexis of course, but I couldn’t get a word between her screaming and crying for help.")
    scrollTxt("The girl, Asuka, had a heart disease which she couldn’t beat. She was suffering from something which would eventually result in her death.")
    scrollTxt("Most likely within the next three months.")
    scrollTxt("Since the moment of her diagnoses, she had been afraid to die.")
    scrollTxt("She had begged more than every patient in the hospital for us to find a cure, but sadly we couldn’t help her.")
    scrollTxt("After a while Asuka started to calm down. She was getting tired of all the screaming and hyperventilating. Then she fell asleep.")
    scrollTxt("\n--------------------------------the next day--------------------------------\n")
    scrollTxt("After I have had my morning coffee, Judy came running towards me. Still groggy from the pretty bad dream that I had tonight, I turned towards her.")
    scrollTxt("""
Dr. Leskinen:
“Morning, Judy.”
""")
    scrollTxt("Dr Judy seemed to be out of breath. Seemed that the message she was about to deliver, was very urgent.")
    scrollTxt("""
Dr. Judy:
“Could you come with me? I need to show you something.”
""")
    scrollTxt("Before I could answer, Dr. Judy grabbed my arm and pulled me to Asuka’s room.")
    scrollTxt("It could be my imagination, but Judy seemed to be a bit tired today. She had darker spots beneath her eyes and seemed a bit more stressful than normal.")
    scrollTxt("\nWhen we arrived at Asuka’s room, she was already sitting up straight in her bed.")
    scrollTxt("""
Dr. Judy:
“Tell Dr. Leskinen what you just told me”.
""")
    scrollTxt("Asuka looked a bit shy. Like she didn’t want to answer the question.")
    scrollTxt("After a few seconds she started explaining.")
    scrollTxt("""
Patient Asuka: 
“Last night I had a dream that went on for a long time. It was a nightmare that seemed to span almost two days. 
In that nightmare, I was floating in space. I was the only one left behind since my crewmates had ejected me. They were all going insane.
I was floating in the emptiness of space. I couldn’t go forward or backward, to the left or right. 
My only option was to float till my oxygen tank was depleted. It started to deplete very slowly. 
And by the time my oxygen tank was empty, I woke up in the hospital.”
""")
    scrollTxt("I started frowning. It couldn’t be, right?\n")

    if(movieInput == "1"):
        scrollTxt("That Asuka got infected, because I forgot to wear my mask yesterday.")
    else:
        scrollTxt("That Asuka got infected due to Alexis getting near her?")

    scrollTxt("If that was the case, it would mean that this virus would be airborne.")
    scrollTxt("That would also mean that Judy and I accidentally infected the entire Emergency Room and the neurological department.")
    scrollTxt("After calming down Alexis yesterday, I went to check on other patients.")
    scrollTxt("When I just started connecting the dots, Judy also explained that she got a long dream.")
    scrollTxt("We were already infected without noticing. I started thinking about how many colleagues I had talked to yesterday.")
    scrollTxt("This hospital was already doomed. The only thing we could do now, was to put the entire hospital in quarantine.")
    scrollTxt("\nI started notifying the rest of the hospital crew. No-one could go in or out this hospital.")
    scrollTxt("The entire hospital had to be on lockdown.")
    scrollTxt("After making sure that no-one could get in or out this hospital, I sat down. I had to find a cure or I would suffer a very bad faith.")
    scrollTxt("One where I would get stuck in dreams for millions of years until I got a dream that would seem endless.")
    scrollTxt("\n----------------------8 hours of lockdown----------------------\n")
    scrollTxt("I started noticing that the hospital crew grew more restless.")
    scrollTxt("The one with a nightshift couldn’t go home and sleep.")
    scrollTxt("Since we only had a small canteen, the food was already eaten by some greedy colleagues.")
    scrollTxt("Patients couldn’t let family visit them. And it started to annoy them to.")
    scrollTxt("Some patients tried to exit their bed and run through the hallways before getting caught and put back in their bed.")
    scrollTxt("\n----------------------- 20 hours of lockdown -------------------\n")
    scrollTxt("After I went to the bathroom, I returned to an empty room where Alexis was supposed to be.")
    scrollTxt("Alexis spend the entire day getting more impatient. By the end of the day, he hadn’t slept in a day and a half.")
    scrollTxt("I panicked slightly. If he got out, he would infect the outside world.")
    scrollTxt("I started searching for him with the entire hospital crew. But we found nothing of him.")
    scrollTxt("He already looked like something that wasn’t human anymore, so he wouldn’t be hard to miss.")
    scrollTxt("After searching for an hour, a colleague found something horrible:")
    scrollTxt("The emergency exit was found left open. Alexis had escaped.")
    scrollTxt("The entire world would soon be infected by his disease, there was no cure and nothing I could do at this point.")
    scrollTxt("In the tempo that Alexis grew more ill by the day, it would mean that the entire world only had around 2 months before everyone couldn’t remember what this world meant to them…")
    
    print(colorDict["red"])
    scrollTxt("\n[Ending unlocked: ‘Same as it ever was’]\n")
    print(colorDict["white"])

def goodEnding():
    scrollTxt("I ran to the breakroom to get some food for Alexis.")
    scrollTxt("I saw some green slimy banana’s lying on the table. They seemed gross, so I skipped them.")
    scrollTxt("I went to the cupboard and grabbed some bread and peanut butter. I prepared some bread with peanut butter for Alexis and returned to the room.")
    scrollTxt("Alexis was in no shape to object, so I gave him the food. He ate it without questioning it.")
    scrollTxt("After a few minutes Alexis began wheezing. Every second he seemed to breathe heavier than the one before.")
    scrollTxt("""
I started panicking. I grabbed his report and there it was: 
•	Allergies: peanuts.
""")
    scrollTxt("I have accidentally triggered his allergic reaction.\n")
    scrollTxt("Alexis started coughing. He was hyperventilating and couldn’t breathe properly anymore.")
    scrollTxt("Before I could grab the oxygen mask, his heart monitor flatlined. ")
    scrollTxt("He was death within seconds and it was all my mistake.")
    scrollTxt("The defibrillator didn’t bring him back afterwards.")
    scrollTxt("I just stood there dumbfounded.")
    scrollTxt("Maybe this was the best for him.")
    scrollTxt("There was no cure or treatment that could have helped him.")
    scrollTxt("He would have gotten longer nightmares every night until he would get a nightmare that would be so long that it wouldn’t contain an ending. ")
    
    print(colorDict["green"])
    scrollTxt("Good ending unlocked: [Eternal peace]")
    print(colorDict["white"])

def jokeEnding():
    scrollTxt("I ran to the breakroom to get some food.")
    scrollTxt("I decided to grab the first thing edible thing I could see. It was the squishy green banana I microwaved a few days ago.")
    scrollTxt("‘Yuk’ I thought and put it on a plate before returning to Alexis Room.")
    scrollTxt("I gave him the plate with ‘food’ on it.")
    scrollTxt("While giving Alexis the plate, I noticed a peculiar smell coming from the hand that touched the banana.")
    scrollTxt("It smelled like a garbage left outside in 30° degrees weather. ")
    scrollTxt("I quickly went to wash my hands while I saw Alexis peeling what’s left of the banana.")
    scrollTxt("He was so tired that he almost seemed like an animatronic. His eyes were almost shut and he moved very slow.")
    scrollTxt("When I returned from washing my hands, the banana was already eaten by Alexis.")
    scrollTxt("He didn’t seem very different than normal.")
    scrollTxt("\n‘so be it’, I thought.")
    scrollTxt("\nI suddenly saw a flash through the windows and heard the sound of squeaking tires. ")
    scrollTxt("I didn’t think much of it. Some kids will use the big empty parking space as a place to test their new vehicles. ")
    scrollTxt("\nI went to report on some other patients when I heard someone running through the hallway.")
    scrollTxt("I thought that it was Dr. Judy, but it was someone I hadn’t seen before.")
    scrollTxt("He looked like a professor with the clothing he wore.")
    scrollTxt("He also had fluffy hair, but I didn’t recognize him. So he didn’t work here.")
    scrollTxt("He ran past me to Alexis' room. I walked back to Alexis room to see what he was going to do.")
    scrollTxt("Visitor hours were already over for today.")
    scrollTxt("When I entered the room, Alexis stood next to his bed leaning on the shoulder of the strange professor.")
    scrollTxt("\nI politely asked the professor to put Alexis back on his bed and if he himself could return to the psych ward.")
    scrollTxt("""
The professor:
“My name is Emmett Brown. I’ve come here from the future. 2050 to be precise. 
In this future Alexis was patient zero of the disease that will destroy mankind. 
I’m here to take him to a lab in the future. To study him and prevent / delay a global disaster. 
If I take him now, he will be gone in this timeline for another 28 years. 
So he will be in a time where they are medically more advanced than they are now.“
""")
    scrollTxt("I stood there dumbfounded. Not knowing what to do.")
    scrollTxt("Will I let Alexis get kidnapped by someone from the psych ward or is he really a time traveler from the future?")
    scrollTxt("For now I seemed to just stand there and see where this would go.")
    scrollTxt("\nAlexis walked with the professor to the parking lot.")
    scrollTxt("\nHe stepped into a, what seemed to be, modified Delorean. Emmett closed both the doors and turned on his vehicle.")
    scrollTxt("He started speeding to the exit of the parking lot when there was a bright flash and some fire trails left where he had driven.")
    scrollTxt("There were no signs of the Delorean crashing into a wall. He really was gone.")
    scrollTxt("Alexis was really taken to the future.  A future where he would be studied and possible be helped.")
    
    print(colorDict["blue"])
    scrollTxt("Ending unlocked: [Not my problem]")
    print(colorDict["white"])

#---------------------------------------------------------------------------------------------

#order of the story
system("cls")
introduction()
firstChoice()

if(boredomInput == "1"):
    readRapport()
elif(boredomInput == "2"):
    microwaveBanana()

talkWithPatient()
atHome()
movieChoice()
if(movieInput == "1"):
    watchMovie()
else:
    goToBed()

tiredPatient()
sleepChoice()
if(sleepInput == "1"):
    neutralEnding()
else:
    scrollTxt("“No, Alexis, you can’t sleep for now. You need to be awake to avoid another dream.”")
    
    if(movieInput == "1"):
        badEnding()
    else:
        panickedPatientChoice()
        
        if(panicInput == "1"):
            badEnding()
        else:
            scrollTxt("\nI have decided to make sure the patient is calm first before he does something irrational.")  
            calmPatientChoice()
    
            if(calmPatientInput == "1"):
                scrollTxt("I will need to give Alexis some food to let him calm down. Can’t think properly on an empty stomach.")               
    
                if(boredomInput == "1"):
                    goodEnding()
                else:
                    jokeEnding()
            else:
                scrollTxt("I grabbed some medicins to calm Alexis down and gave him a glass water to swallow his pills.")
                scrollTxt("He seemed to calm rather quickly.\n")
                neutralEnding()


