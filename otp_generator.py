import random
all = "1234567890"
length = 4
print("Enter 'M' to create 4 digit otp and 'Q' to quit")

while True:
	choice = input("Enter your choise : ").lower()
	if(choice == "m"):
		otp = "".join(random.sample(all,length))
		print(otp)
	elif(choice == "q"):
		break
	else:
		pass