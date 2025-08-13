import pyttsx3
import webbrowser as wb
import wikipedia as wiki
import time
import os
import pyjokes

engine = pyttsx3.init()

while True:
    a = input("You : ").lower()
    
    if a == "hello" or a == "hi":
        print("Jarvis : Hi there how can i assist you sir")
        engine.say("hi there how can i assist you sir")
        engine.runAndWait()
        
    elif a == "introduce yourself" or a == "who are you":
        print("Jarvis : I am jarvis your own ai assistant. I will assist you 24 hours of a day and 7 days of weeks")
        engine.say("I am jarvis your own ai assistant i will assist you 24 hours of a day and 7 days of weeks")
        engine.runAndWait()
        
    elif a == "what is the time":
        current_time = time.strftime("%H:%M")
        print(f"Jarvis : The current time is {current_time}")
        engine.say(f"The current time is {current_time}")
        engine.runAndWait()
    
    elif a.startswith("open "):
        web = a[5:]
        print(f"Jarvis : Opening {web}")
        engine.say(f"opening {web}")
        engine.runAndWait()
        wb.open(f"https://{web}.com")
    
    elif a.startswith("tell me about "):
        topic = a[14:]
        try:
            info = wiki.summary(topic, sentences=2)
            print("Jarvis :", info)
            engine.say(info)
            engine.runAndWait()
        except:
            print(f"Jarvis : sorry but i can't give the information about {topic}. Please check your internet connection")
            engine.say(f"sorry but i cannot give the information about {topic}. Please check your internet connection")
            engine.runAndWait()
    
    elif a.startswith("what is "):
        expression = a[8:]
        try:
            answer = eval(expression)
            print("Jarvis : The answer is", answer)
            engine.say(f"The answer is {answer}")
            engine.runAndWait()
        except:
            print("Jarvis : There is some problem sir.")
            engine.say("There is some problem sir")
            engine.runAndWait()
            
    elif a == "":
        pass
    
    elif a == "exit" or a == "bye":
        print("Jarvis : Good bye sir have a nice day sir")
        engine.say("Good bye sir have a nice day sir")
        engine.runAndWait()
        break
        
    elif a == "clear":
        os.system("cls" if os.name == "nt" else "clear")
    
    elif a == "tell me a joke":
        joke = pyjokes.get_joke()
        print("Jarvis :", joke)
        engine.say(joke)
        engine.runAndWait()
        
    else:
        print("Jarvis : Sorry but i can't understand your command ")
        engine.say("Sorry but i cannot understand your command")
        engine.runAndWait()