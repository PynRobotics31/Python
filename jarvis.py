import pyttsx3
import webbrowser as wb
import wikipedia as wiki
import os
import time 

def speak(audio):
    engine  = pyttsx3.init("sapi5")
    engine.setProperty("rate",170)
    engine.setProperty("volume",1.0)
    engine.stop()
    engine.say(audio)
    engine.runAndWait()

while True:
    a = input("You : ").lower()

    if(a == "hello" or a=="hi"):
        print("Jarvis : Hi there how can i assist you sir")
        speak("Hi there how can i assist you sir")
    
    elif(a == "who are you" or a == "introduce yourself"):
        print("Jarvis : I am Jarvis, your personal ai assistant. I will assist you 24 hours of a days and 7 days of week")
        speak("I am Jarvis, your personal ai assistant. I will assist you 24 hours of datys and 7 days of week")

    elif(a == "what is the time"):
        time = time.strftime("%H:%M")
        print(f"Jarvis : The current time is {time}")
        speak(f"The current time is {time}")
    
    elif(a.startswith("open ")):
        web = a[5:]
        print(f"Jarvis : Opening {web}")
        speak(f"Opening {web}")
        wb.open(f"https://{web}.com")
    
    elif(a.startswith("tell me about ")):
        data = a[14:]
        try:
            info = wiki.summary(data)
            print(f"Jarvis : {info}")
            speak(info)
        except:
            print(f"Jarvis : Sorry but i can't give you the information about {data}")
            speak(f"Sorry but i can't give you the information about {data}")
    
    elif(a == "clear"):
        os.system("cls")

    elif(a == ""):
        pass

    else:
        print("Jarvis : Sorry but i can't understand your command")
        speak("Sorry but i can't understand your command")