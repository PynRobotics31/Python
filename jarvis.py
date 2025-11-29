import webbrowser as wb
import pyjokes
import time
import os
import datetime
import pyttsx3
import requests
import json
import wikipedia as wiki
from deep_translator import GoogleTranslator
import smtplib
def speak(audio):
    engine = pyttsx3.init("sapi5")
    engine.say(audio)
    engine.runAndWait()

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
    a = input('You : ').lower()

    if(a == "hello" or a == "hi"):
        print("Jarvis : Hi there")
        speak("hi there")
    
    elif(a == "what is the time" or a == "tell me the time" or a=="what is the time"):
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

    elif(a == "open excel"):
        print("Jarvis : Opening Excel")
        speak("Opening excel")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
    
    elif(a == "open calculator"):
        print("Jarvis : Opening calculaor")
        speak("Opening calculaor")
        os.startfile("calc.exe")
    
    elif(a == "open power point"):
        print("Jarvis : Opening power point")
        speak("Opening power point")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")

    elif(a == "open vscode"):
        print("Jarvis : Opening Vscode")
        speak("Opening vscode")
        os.startfile(r"C:\Users\Kushadhaj Betal\AppData\Local\Programs\Microsoft VS Code\Code.exe")

    elif(a == "open word" or a == "open word 365" or a == "ms word"):
        print("Jarvis : Opening Word 365")
        speak("Opening Word 365")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
    
        
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
        except Exception as e:
            print(f"Jarvis : I am sorry but i can't give you the information about {query}")
            print(f"Jarvis : Problem is {e}")
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
        joke = pyjokes.get_joke()
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
        
    elif(a.startswith("play ")):
        song = a[5:]
        print(f"Jarvis : Playing {song}")
        speak(f"Plyaing {song}")
        wb.open(f"https://music.youtube.com/search?q={song}")
        
    elif(a == "bye" or a =="exit"):
        print("Jarvis : Ok bye have a nice day")
        speak("Ok bye have a nice day")
        break
    elif(a.startswith("weather report of ")):
        temp_query=a[18:]
        try:
            apikey = "7040ea904442a45d6950ba584410ce59"
            
            baseURL= "https://api.openweathermap.org/data/2.5/weather?q="
            
            cityname = temp_query
            
            completeURL = baseURL+ cityname+"&appid=" + apikey
            response =requests.get(completeURL)
            
            data= response.json()
            print(f"Jarvis : Current weather of {cityname}")
            speak(f"Current weather of {cityname}")
            print("Current Tempreture : ",data["main"]["temp"])    		
            print("Current Tempreture Feels like : ",data["main"]["feels_like"])    		
            print("Maximum Tempreture : " ,data["main"]["temp_max"]) 		
            print("Maximum Tempreture : ",data["main"]["temp_min"])   		
            print("Pressure: ",data["main"]["pressure"]) 		
            print("Humidity : ",data["main"]["humidity"])		
            print("Sea Level :",data["main"]["sea_level"])
            print("Groud Level :",data["main"]["grnd_level"])
    	
        except Exception as a:
            print(f"Jarvis : Sorry sir but i can't give you the weather report. This problem generate for {a}")

    elif a.startswith("send message to "):
    
        users = {
            
            "mom":"email id",
            "soumyadip da": "email id"
        }
        user = a[16:]
        if(user in users):
            message = input("Jarvis : Enter the text to send : ")
            reciver = users[user]
            try:
                
                
                connection = smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("subhamkumarbetal2010@gmail.com","jynv aanv gsox qkah")
                connection.sendmail(
                    from_addr="subhamkumarbetal2010@gmail.com",
                    to_addrs= reciver,
                    msg=message
                )
                print(f"Jarvis : Message Succesfully send to {user}")
                speak(f"Message Succesfully send to {user}")
            except Exception as g:
                print(f"Jarvis : Message can't be sended. Problem is {g}")

        else:
            print(f"Jarvis : {user} is not saved")
    
    elif(a.startswith("translate ")):
        lang = a[10:]
        try:
            translated_taxt = GoogleTranslator(source="auto",target="bn").translate(lang)
            print(f"Jarvis : Translated meaning of {lang} is {translated_taxt}")
            speak(f"Translated meaning of {lang} is {translated_taxt}")
        except Exception as f:
            print(f"Jarvis : Sorry but i can't translate {lang}")
            print(f"Jarvis : Problem {f}")
            speak(f"Sorry but i can't translate {lang}")
    
    elif(a.startswith("give me some images of ")):
        img = a[18:]
        print(f"Jarvis : Searching in internet for {img} image")
        speak(f" Searching in internet for {img} image")
        wb.open(f"https://unsplash.com/s/photos/{img}")
    else:
        print("Jarvis : Sorry but i don't understand your command sir")
        speak("Sorry but i don't understand your command sir")
