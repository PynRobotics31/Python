import pywhatkit as kit
import datetime

number = input("Enter the phone number (+91) : ")

message = input("Enter your message : ")

now = datetime.datetime.now()
hour = now.hour
minute = now.minute+1

try:
	kit.sendwhatmsg(number,message,hour,minute)
	print("Message succesfully sended")
	
except Exception as e:
	print("Can't send message ")
	print("Problem : ",e)