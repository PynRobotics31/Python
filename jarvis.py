import pyttsx3
import webbrowser as wb
import wikipedia as wiki
import os
import time
import pyjokes
import datetime
import requests
import json
import pywhatkit
from deep_translator import GoogleTranslator

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
    speak("Good Afternoon sir")
    
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
        except Exception as e:
            print(f"Jarvis : Sorry, I can't give information about {topic}.")
            print(f"Jarvis : The problem is for {e}")
            
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
    
    elif(a == "shutdown"):
    	os.system("shutdown -s")
    
    elif(a.startswith("weather report of ")):
    	temp_query=a[18:]
    	try:
    		apikey = "7040ea904442a45d6950ba584410ce59"
    		
    		baseURL= "https://api.openweathermap.org/data/2.5/weather?q="
    		
    		cityname = temp_query
    		
    		completeURL = baseURL+ cityname+"&appid=" + apikey
    		
    		response =requests.get(completeURL)
    		
    		data= response.json()
    		
    		print("Current Tempreture : ",data["main"]["temp"])    		
    		print("Current Tempreture Feels like : ",data["main"]["feels_like"])    		
    		print("Maximum Tempreture : " ,data["main"]["temp_max"]) 		
    		print("Maximum Tempreture : ",data["main"]["temp_min"])   		
    		print("Pressure: ",data["main"]["pressure"]) 		
    		print("Humidity : ",data["main"]["humidity"])		
    		print("Sea Level :",data["main"]["sea_level"])
    		print("Groud Level :",data["main"]["grnd_level"])
    		
    	except Exception as e:
    		print(f"Jarvis : Sorry sir but i can't give you the weather report. This problem generate for {e}")
    		
    elif(a.startswith("translate ")):
    	
    	try:
    		text = a[10:]
    		translate = GoogleTranslator(source="auto",target="bn").translate(text)
    		print(f"Jarvis : Translated Meaning of {text} is : {translate}")
    		speak(f"Translated Meaning of {text} is {translate}")
    		
    	except Exception as e:
    		print("Jarvis : Sorry cannot translate ")
    		
    		print(f"Jarvis : The problem is {e}")
    		speak("Sorry cannot translate")
    
    elif(a.startswith("send message to ")):
    	
    	now = datetime.datetime.now()
    	hour = now.hour
    	minute = now.minute+1
    	
    	users = {
    	    "shayan":"+918158098686",
    	    "mom":"+919851807533",
    	    "sister":"+917319085574",
    	    "dad":"+918172064168",
    	    "sayan purakit":"+917908036963"
    	}
    	user=a[16:]
    	if(user in users):
    		try:
    			message = input("Jarvis : Enter message to send")
    			pywhatkit.sendwhatmsg(users[user],message,hour,minute)
    		except Exception as e:
    			print(f"Jarvis : Cannot send message to {user}. The problem is {e}")
    			
    	else:
    		print(f"Jarvis : {user} is not saved in chat list")
    		
    else:
        print("Jarvis : Sorry but I can't understand your command")
        speak("Sorry but I cannot understand your command")
