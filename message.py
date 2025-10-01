import pywhatkit as kit
import datetime
message = input("Enter the text to send : ")
phone = input("Enter the number to send the message : ")
now=datetime.datetime.now()
hour = now.hour
minute = now.minute+2
print(f"The time format is {hour , minute}")
try:
    kit.sendwhatmsg(phone,message,hour,minute)
    print(f"Succesfully send message to {phone}")

except Exception as e:
    print("Message can't be send ")
    print(f"Problem : {e}")

