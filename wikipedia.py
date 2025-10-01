import wikipedia
try:
	a = input("enter what you search:")
	result = wikipedia.summary(a)
	print(result)
except:
	print("sorry",a,"is not founded, plase check your internet conection")