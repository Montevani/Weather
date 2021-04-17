import requests
from pprint import pprint as pp
API_Key = '157b2d0bef11e1fafc79c4aadf1858a4' #I sincerely don't care about this API key, feel free to steal it
city = input ("Please enter your city's name: ")
url = "http://api.openweathermap.org/data/2.5/weather?appid=" +API_Key+"&q="+city
weather_data = requests.get(url).json()
pp(weather_data)
