try:
	import wikipedia
	a = input("enter what you search:")
	result = wikipedia.search(a)
	for search in result:
		print(search)
		print(wikipedia.page(search).summary)
except:
	print("sorry",a,"is not founded, plase check your internet conection")