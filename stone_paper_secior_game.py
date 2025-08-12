import random
choise = ["stone","paper","secior"]
len = 1
while True:
	you = input("Enter your choise : ")
	robo = "".join(random.sample(choise,len))
	print("robot : ",robo)
	if(you=="stone" and robo == "stone" or you=="paper" and robo=="paper" or you=="secior" and robo=="secior"):
		print("match draw")
		
	elif(you =="stone" and robo=="secior" or you=="paper" and robo=="stone" or you=="secior" and robo=="paper"):
		print("you win")
		
	elif(you =="secior" and robo=="stone" or you=="stone" and robo=="paper" or you=="paper" and robo=="secior"):
		print("robot win")
	else:
		print("You can input only stone ,paper or secior")