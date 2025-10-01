import phonenumbers
from phonenumbers import geocoder,timezone,carrier
while True:
    number = input("Enter the phone number with country code (enter exit for shutdown the window): ").lower()
    phone = phonenumbers.parse(number)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone,"en")
    reg = geocoder.description_for_number(phone,"en")
    print(phone)
    print(time)
    print("sim card ",car)
    print(reg)
    if(number == "exit"):
        print("shuting down")
        break