import datetime
import time
import os
import wikipedia
import webbrowser as wb
 
hour = int(datetime.datetime.now().hour)

if hour >= 0 and hour < 12:
    print("Good Morning sir")
elif hour >= 12 and hour < 18:
    print("Good Afternoon sir")
else:
    print("Good Evening sir")

print("How can I assist you")

db = {}

while True:
    a = input("You: ").lower()

    if a == "hello":
        print("Jarvis: Hi there")

    elif(a == "introduce yourself"):
    	print("Jarvis : hello i am jarvis your personal ai assistant. I will assist you 24 hours of day and 7 days of week")

    elif a == "how are you":
        print("Jarvis: I am just a computer program, but thanks for asking")

    elif a == "bye":
        print("Jarvis: Goodbye, have a nice day")
        break

    elif a == "who are you":
        print("Jarvis: I am your personal AI")

    elif a.startswith("open "):
        app = a[5:]
        print("Jarvis: Opening", app)
        wb.open(f"https://www.{app}.com")

    elif a == "what is the time":
        print("Jarvis: Current time is", time.strftime("%H:%M"))

    elif a == "open google maps":
        print("Jarvis: Opening Google Maps")
        url = "https://maps.google.com"
        wb.open(url)

    elif a == "clear":
        os.system("clear")  

    elif a.startswith("search in internet "):
        wiki = a[19:]
        try:
            result = wikipedia.summary(wiki)
            print(result)
        except:
            print(f"Jarvis: Sorry sir, I can't get the information about {wiki}, please check your internet connection")
    
    elif a == "open youtube music":
        webbrowser.open("https://music.youtube.com")
        print("Jarvis: Opening YouTube Music")

    elif a.startswith("search in google "):
        search = a[16:]
        print("Jarvis: Searching in Google", search)
        wb.open("https://www.google.com/search?q=" + search)

    elif a.startswith("search in youtube "):
        sy = a[18:]
        print("Jarvis: Searching in YouTube", sy)
        wb.open("https://www.youtube.com/results?search_query=" + sy)
    elif(a.startswith("what is ")):
    	sum = a[8:]
    	print(f"Jarvis : the answer is {eval(sum)}")
    else:
        print("Bot: I don’t understand your command")