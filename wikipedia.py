try:
	import wikipedia as wiki
	user = input(">>> ")
	data = wiki.summary(user)
	print(data)
except Exception as e:
	print("Problem ",e)