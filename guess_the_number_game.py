import random
guess=random.randint(1,10)
print(guess)
print("Guess number 1 to 10 ")
while True:
	player = int(input("Your turn : "))
	if(player == guess):
		print("You win")
		break
	else:
		print("not matched buddy")