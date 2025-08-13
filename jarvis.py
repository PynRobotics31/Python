import pyttsx3
import webbrowser as wb
import wikipedia as wiki
import time
import os
import pyjokes

engine = pyttsx3.init()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

while True:
    a = input("You : ").lower()
    
    if a == "hello" or a == "hi":
        print("Jarvis : Hi there how can i assist you sir")
        speak("hi there how can i assist you sir")
    
        
    elif a == "introduce yourself" or a == "who are you":
        print("Jarvis : I am jarvis your own ai assistant. I will assist you 24 hours of a day and 7 days of weeks")
        speak("I am jarvis your own ai assistant i will assist you 24 hours of a day and 7 days of weeks")
        
        
    elif a == "what is the time":
        current_time = time.strftime("%H:%M")
        print(f"Jarvis : The current time is {current_time}")
        speak(f"The current time is {current_time}")
        
    
    elif a.startswith("open "):
        web = a[5:]
        print(f"Jarvis : Opening {web}")
        speak(f"opening {web}")
        wb.open(f"https://{web}.com")
    
    elif a.startswith("tell me about "):
        topic = a[14:]
        try:
            info = wiki.summary(topic, sentences=2)
            print("Jarvis :", info)
            speak(info)
            
        except:
            print(f"Jarvis : sorry but i can't give the information about {topic}. Please check your internet connection")
            speak(f"sorry but i cannot give the information about {topic}. Please check your internet connection")
           
    
    elif a.startswith("what is "):
        expression = a[8:]
        try:
            answer = eval(expression)
            print("Jarvis : The answer is", answer)
            speak(f"The answer is {answer}")
            
        except:
            print("Jarvis : There is some problem sir.")
            speak("There is some problem sir")
            
            
    elif a == "":
        pass
    
    elif a == "exit" or a == "bye":
        print("Jarvis : Good bye sir have a nice day sir")
        speak("Good bye sir have a nice day sir")
        break
        
    elif a == "clear":
        os.system("cls" if os.name == "nt" else "clear")
    
    elif a == "tell me a joke":
        joke = pyjokes.get_joke()
        print("Jarvis :", joke)
        speak(joke)
        
    
    else:
        print("Jarvis : Sorry but i can't understand your command ")
        speak("Sorry but i cannot understand your command")
        