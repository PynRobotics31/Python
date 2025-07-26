from googletrans import Translator
translate = Translator()
while True:
	text=input("Enter the text : ")
	translated_text=translate.translate(text,dest="bn")
	print("translated language is : ",translated_text.text)