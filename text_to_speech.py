from gtts import gTTS
text = "Hello this voice is created by gtts(google text to speach) module"
language = "en"
speech = gTTS(text=text,lang=language,slow=False)
speech.save("voice.mp3")