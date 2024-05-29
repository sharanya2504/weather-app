import requests

apiid = '057cb0855e2cccb44eca5210d7b524a7'

print("WELCOME TO WEATHER APP")
city= input("Enter The Location:")
weather_data = (requests.get
                (f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={apiid}"))

if weather_data.json()['cod'] == '404':
    print("City not found!")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    humidity = weather_data.json()['main']['humidity']
    maxtemp = weather_data.json()['main']['temp_max']
    mintemp = weather_data.json()['main']['temp_min']


print(f"Weather  : {weather}")
print(f"Temperature : {temp}ºC")
print(f"Humidity  : {humidity}")
print(f"Maximum Temperature  : {maxtemp}ºC")
print(f"Minimum Temperature : {mintemp}ºC")
