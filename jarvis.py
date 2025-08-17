import pyttsx3
import wikipedia as wiki
import webbrowser as wb
import os
import time
import pyjokes
import datetime

def speak(audio):
    engine = pyttsx3.init("sapi5")
    engine.getProperties("rate",170)
    engine.getProperty("volume",1.0)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    print("Good Morning sir")
    speak("Good Morning sir")
    
elif hour >= 12 and hour < 18:
    print("Good Afternoon sir")
    sepak("Good Afternoon sir")
    
else:
    print("Good Evening sir")
    speak("Good Evening sir")

while True:
    a = input("You : ").lower()

    if a == "hello" or a == "hi":
        print("Jarvis : Hi there how can I assist you sir")
        speak("hi there how can i assist you sir")

    elif a == "who are you" or a == "introduce yourself":
        print("Jarvis : I am Jarvis your own AI assistant. I will assist you 24 hours a day and 7 days a week")
        speak("I am Jarvis your own AI assistant. I will assist you 24 hours a day and 7 days a week")

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
            print(f"Jarvis : Sorry, I can't give information about {topic}. Please check your internet connection")
            speak(f"Sorry, I cannot give information about {topic}. Please check your internet connection")

    elif a == "exit" or a == "bye":
        print("Jarvis : Goodbye sir, have a nice day!")
        speak("Goodbye sir, have a nice day")
        break
        
    elif(a.startswith("search in google")):
    	sg = a[16:]
    	print(f"Jarvis : Searching in google {sg}")
    	speak(f"searching in google {sg}")
    	wb.open(f"https://www.google.com/search?q={sg}")
    
    elif(a.startswith("search in youtube ")):
    	sy = a[18:]
    	print(f"Jarvis : searching in youtube {sy}")
    	speak(f"searching in youtube {sy}")
    	wb.open(f"https://www.youtube.com/results?search_query={sy}")
    	
    elif(a == "tell me a joke"):
    	joke = pyjokes.get_joke()
    	print(f"Jarvis : {joke}")
    	speak(joke)
    	
    elif(a == "clear"):
    	os.system("clear")
    	
    elif(a.startswith("play ")):
    	song = a[5:]
    	print(f"Jarvis : Playing {song}")
    	speak(f"playing {song}")
    	wb.open(f"https://music.youtube.com/search?q={song}")
    
    elif(a == ""):
    	pass
    
    elif(a.startswith"what is "):
    	math = a[8:]
    	try:
    		print(f"Jarvis : The answer is {eval(math)}")
    		speak(f"The answer is {eval(math)}")
    	except:
    		print("Jarvis : There is some problem please try again")
    
    elif(a.startswith("play ")):
    	song = a[5:]
    	print(f"Jarvis : Playing {song}")
    	speak(f"Playing {song}")
    	wb.open(f"https://music.youtube.com/search?q={song}")
    
    elif a.startswith("search in youtube "):
        sy = a[18:]
        print("Jarvis: Searching in YouTube", sy)
        speak(f"serching in youtube {sy}")
        wb.open("https://www.youtube.com/results?search_query=" + sy)
        
    elif a.startswith("search in google "):
        search = a[16:]
        print("Jarvis: Searching in Google", search)
        speak(f"searching in google {search}")
        wb.open("https://www.google.com/search?q=" + search)
    
    else:
        print("Jarvis : Sorry but I can't understand your command")
        speak("Sorry but I cannot understand your command")
