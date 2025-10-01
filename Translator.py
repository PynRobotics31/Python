from deep_translator import GoogleTranslator

while True:
    lang = input("Enter the text : ").lower()
    translated_taxt = GoogleTranslator(source="auto",target="bn").translate(lang)
    print("Translated text is : ",translated_taxt)
    
