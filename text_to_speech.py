from gtts import gTTS
text = "sala kuttar bache motger chod bhen chod gud marani bal choda khankir chele bal ar choda tor gube"
language = "en"
speech = gTTS(text=text,lang=language,slow=False)
speech.save("voice.mp3")