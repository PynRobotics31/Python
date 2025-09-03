import requests, json

apikey = "7040ea904442a45d6950ba584410ce59"

baseURL= "https://api.openweathermap.org/data/2.5/weather?q="

cityname = input("Enter your City : ")

completeURL = baseURL+ cityname+"&appid=" + apikey

response =requests.get(completeURL)

data= response.json()

print("Current Tempreture : ",data["main"]["temp"])

print("Current Tempreture Feels like : ",data["main"]["feels_like"])

print("Maximum Tempreture : ",data["main"]["temp_max"])

print("Maximum Tempreture : ",data["main"]["temp_min"])

