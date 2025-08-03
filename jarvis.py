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

hist = []
while True:
    a = input("You: ").lower()
    hist.append(a)
    if(a == "hello" or a=="hi"):
        print("Jarvis: Hi there")

    elif(a == "introduce yourself" or a == "who are you"):
    	print("Jarvis : hello i am jarvis your personal ai assistant. I will assist you 24 hours of day and 7 days of week")

    elif a == "how are you":
        print("Jarvis: I am just a computer program, but thanks for asking")

    elif a == "bye" or a== "exit":
        print("Jarvis: Goodbye, have a nice day")
        break

    elif a == "who are you":
        print("Jarvis: I am jarvis your personal AI")

    elif a.startswith("open "):
        app = a[5:]
        print("Jarvis: Opening", app)
        wb.open(f"https://www.{app}.com")

    elif a == "what is the time" or a == "tell me the time":
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
        try:
    	    sum = a[8:]
    	    print(f"Jarvis : the answer is {eval(sum)}")
        except:
            print("Jarvis : There is problem. Please try again later")
    
    elif(a == "make task"):
        todo = []
        while True:
            task = input("Enter your task(enter done to skip) : ")
            if task == "done":
                print("todo is saved")
                break
            todo.append(task)
    elif(a == "show task"):
        try:
            for i in todo:
                print(i)
        except:
            print("Jarvis : no any task is saved")
    
    elif(a == "delete task"):
        del_task = input("Enter thc9e task that you want to delete : ")
        if del_task in todo:
            print("Jarvis : task deleted")
            todo.remove(del_task)
        else:
            print("Jarvis : the task is not in list")
            
    elif(a == "delete all task"):
    	try:
    	    for j in todo:
    		    todo.remove(j)
    	except:
    		print("Jarvis : No any taks is saved")
    elif(a == ""):
    	pass
    	
    elif(a == "history"):
    	try:
    		for b in hist:
    			print(b)
    	except:
    		print("Jarvis : Empty history")
    
    elif(a == "play my favorite song"):
    	print("Jarvis : playing your favorite song")
    	song = "https://youtu.be/Ru7CxHauVFM?si=2V7I9t_isV4jNFya"
    	wb.open(song)
    	
    else:
        print("Jarvis: I don’t understand your command")

