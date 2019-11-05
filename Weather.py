import requests
api_address='http://api.openweathermap.org/data/2.5/weather?appid=343c877db056b953447e1b48bb5f6421&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()
format_add = json_data['base']
float("{0:.2f}".format(json_data['main']['temp']-273.15))
print("Current Temp={0:.1f}°C".format(json_data['main']['temp']-273.15))
print("Pressure={0:d}mBar".format(json_data['main']['pressure']))
print("Humidity={0:d}%".format(json_data['main']['humidity']))
