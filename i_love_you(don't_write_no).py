import os
a = input("Do you love me or not : ")
for i in range(2):
    if a == "yes":
        print("I love you too")     

    if a == "no":
        print("Your system will shutdown at 5 seconds")
        os.system("shutdown -s -t 5")

    else:
        print("you can only chose yes or no")