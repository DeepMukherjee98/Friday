import  pyttsx3 as p
import os
import random
import math
import calendar
from datetime import date, datetime

#import vlc

while True:

    cmd=["Waiting for your command","What is my next task","What would you like me to do"]
    a=random.choice(cmd)
    p.speak(a)
    x=input(f"{a} : ")
    x=x.lower()

    if ("chrome" in x or "google" in x) and ("open" in x):
        p.speak('Opening Chrome')
        os.system("chrome")

    elif ("atom" in x or "python" in x) and ("open" in x):
        p.speak('Opening Atom')
        os.system("atom")

    elif ("notepad" in x or "editor" in x) and ("open" in x):
        p.speak('Opening Notepad')
        os.system("notepad")

    elif ("command prompt" in x or "cmd" in x) and ("open" in x):
        p.speak('Opening Command prompt')
        os.system("cmd")

    elif ("slack" in x ) and ("open" in x):
        p.speak('Opening Slack')
        os.system("slack")

    elif ("virtual box" in x or "vmware" in x or "vmbox" in x) and ("open" in x):
        p.speak('Opening Virtual box')
        os.system("VirtualBox")

    elif ("whatsapp" in x or "whatsup" in x) and ("open" in x):
        p.speak('Opening Whatsapp')
        os.system("WhatsApp")

    elif ("media player" in x or "player" in x or "wmplayer" in x) and ("open" in x):
        p.speak('Openning Media player')
        os.system("wmplayer")

    elif ("quit" in x or "close" in x) and ("friday" in x):
        p.speak('Closing Friday')
        break

    elif("add" in x or 'adddition' in x):
        numbers = []
        for word in x.split():
            if word.isdigit():
                numbers.append(int(word))
        sum=sum(numbers)
        s='The sum is '+str(sum)
        p.speak(f"{s}")
        print(f"{s}")

    elif("minus" in x or 'substract' in x):
        numbers = []
        for word in x.split():
            if word.isdigit():
                numbers.append(int(word))
        dif=numbers[0]-numbers[1]
        s='The difference is '+str(dif)
        p.speak(f"{s}")
        print(f"{s}")

    elif("multiply" in x or 'multiplication' in x):
        numbers = []
        for word in x.split():
            if word.isdigit():
                numbers.append(int(word))
        prod=math.prod(numbers)
        s='The multiplication is '+str(prod)
        p.speak(f"{s}")
        print(f"{s}")

    elif("divide" in x or 'division' in x):
        numbers = []
        for word in x.split():
            if word.isdigit():
                numbers.append(int(word))
        if numbers[1]==0:
            p.speak("The result will be infinite")
            print('The result will be infinite')
        else:
            s=numbers[0]/numbers[1]
            s='The division is '+str(s)
            p.speak(f"{s}")
            print(f"{s}")

    elif "date" in x and ("today" in x or "today's" in x):
        today = date.today()
        t="Today's date: is "+str(today)
        p.speak(t)

    elif "what is the time" in x or "what's the time " in x or "what is the time now" in x or "what's the time now" in x or "time now" in x:
        now = datetime.now()
        current_time = now.strftime("%H:%M:")
        t="Current Time is "+str(current_time)
        p.speak(t)

    elif "day" in x and ("today's" in x or "today" in x):
        g=[]
        date=str(date.today())
        g=date.split("-")
        s=g[2]+" "+g[1]+" "+g[0]
        born = datetime.strptime(s, '%d %m %Y').weekday()
        t="The day should be "+str(calendar.day_name[born])
        p.speak(t)

    elif "day" in x :
        date=[]
        for word in x.split():
            if word.isdigit():
                date.append(int(word))
        date=str(date[0])+" "+str(date[1])+" "+str(date[2])
        born = datetime.strptime(date, '%d %m %Y').weekday()
        t="The day should be "+str(calendar.day_name[born])
        p.speak(t)

    else :
        p.speak("Don't Support yet")
