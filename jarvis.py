import webbrowser as wb
import wikipedia as wiki
import pyjokes
import time
import os
import datetime
import pyttsx3

def speak(audio):
    engine = pyttsx3.init("sapi5")
    engine.say(audio)
    engine.runAndWait()

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    print("Good Morning sir")
    
elif hour >= 12 and hour < 18:
    print("Good Afternoon sir")

else:
    print("Good Evening sir")


while True:
    a = input('You : ').lower()

    if(a == "hello" or a == "hi"):
        print("Jarvis : Hi there")
        speak("hi there")
    
    elif(a == "what is the time" or a == "tell me the time"):
        time = time.strftime("%H:%M")
        print(f"Jarvis : The current time is {time}")
        speak(f"The current time is {time}")
    
    elif(a == "who are you" or a == "introduce yourself" or a == "what is your name"):
        print("Jarvis : I am jarvis your personal ai assistant. I will assist you 24 hours of a day and 7 days of week")
        speak("I am jarvis your personal ai assistant. I will assist you 24 hours of a day and 7 days of week")

    elif(a == ""):
        pass

    elif(a == "clear"):
        os.system("cls")

    elif(a == "open notepad"):
        print("Jarvis : Opening notepad")
        speak("Opening notepad")
        os.system("notepad")
    
    elif(a.startswith("open ")):
        web = a[5:]
        print(f"Jarvis : Opening {web}")
        speak(f"Opening {web}")
        wb.open(f"https://{web}.com")

    elif(a.startswith("tell me about ")):
        query = a[14:]
        try:
            data = wiki.summary(query)
            print(f"Jarvis : {data}")
            speak(data)
        except:
            print(f"Jarvis : I am sorry but i can't give you the information about {query}")
            speak(f"I am sorry but i can't give you the information about {query}")
    
    elif(a.startswith("search in youtube ")):
        sy = a[18:]
        print(f"Jarvis : Searching in youtube {sy}")
        speak(f"Searching in youtube {sy}")
        wb.open(f"https://youtube.com/results?search_query={sy}")

    elif(a.startswith("search in google ")):
        sg = a[17:]
        print(f"Jarvis : Searching in google {sg}")
        speak(f"Searching in google {sg}")
        wb.open(f"https://www.google.com/search?q={sg}")
    
    elif(a == "tell me a joke"):
        joke = pyjokes.get_jokes()
        print(f"Jarvis : {joke}")
        speak(joke)
    
    elif(a.startswith("what is ")):
        sum = a[8:]
        try:
            quetion = eval(sum)
            print(f"Jarvis : The answer is {quetion}")
            speak(f"The answer is {quetion}")
        except:
            print("Jarvis : I can't answering you about your sum There can be some problem ")
            speak("I can't answering you about your sum There can be some problem ")

    elif(a == "bye" or a =="exit"):
        print("Jarvis : Ok bye have a nice day")
        speak("Ok bye have a nice day")
        break

    else:
        print("Jarvis : Sorry but i don't understand your command sir")
        speak("Sorry but i don't understand your command sir")
