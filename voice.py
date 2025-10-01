import pyttsx3
#engine = pyttsx3.init("sapi5")
def speak(audio):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate",170)
    engine.setProperty("volume",1.0)
    engine.stop()
    engine.say(audio)
    engine.runAndWait()
while True:
    a = input("enter a text (enter 'exit' to stop):")
    
    if a == "exit":
        break
    else:
        speak(a)