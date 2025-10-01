import random
choise = ["stone","paper","secior"]
len = 1
while True:
    robo = "".join(random.sample(choise,len))
    you = input("Enter your choise (exit for end the game) : ")
    print("robot :",robo)

    if(you == "stone" and robo=="stone" or you=="secior" and robo=="secior" or you=="paper"and robo=="paper"):
        print("result : match draw")
    
    elif(you == "stone" and robo=="secior" or you=="paper" and robo=="stone" or you=="secior"and robo=="paper"):
        print("result : you win")
    
    elif(you == "secior" and robo=="stone" or you=="stone" and robo=="paper" or you=="paper"and robo=="secior"):
        print("resule : robot win")
    
    elif(you == "exit"):
        print("match stoped")
        break
    else:
        print("you can enter stone , paper or secior")