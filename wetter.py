#API : http://api.openweathermap.org/data/2.5/weather?id=2873759&appid=d203ea0b51246caa695ff174dfca7fe8

import urllib.request
import json

url = 'http://api.openweathermap.org/data/2.5/weather?id=2873759&appid=d203ea0b51246caa695ff174dfca7fe8'

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)

data = json.load(response)
#print ("Wind:", data['wind'])

wind = data['wind']

wind_kmh = wind['speed'] * 3.6

print ('Windspeed:', wind['speed'], 'm/s =', wind_kmh, 'km/h')

wind_kmh = wind['speed'] * 3.6
wind_deg_nr = wind['deg']
wind_deg_dct = wind_deg_nr / 22.5
wind_deg_lt = "N"

if wind_deg_dct <= 0:
    wind_deg_lt = "N"
elif wind_deg_dct <= 1:
    wind_deg_lt = "NNE"
elif wind_deg_dct <= 2:
    wind_deg_lt = "NE"
elif wind_deg_dct <= 3:
    wind_deg_lt = "ENE"
elif wind_deg_dct <= 4:
    wind_deg_lt = "E"
elif wind_deg_dct <= 5:
    wind_deg_lt = "ESE"
elif wind_deg_dct <= 6:
    wind_deg_lt = "SE"
elif wind_deg_dct <= 7:
    wind_deg_lt = "SSE"
elif wind_deg_dct <= 8:
    wind_deg_lt = "S"
elif wind_deg_dct <= 9:
    wind_deg_lt = "SSW"
elif wind_deg_dct <= 10:
    wind_deg_lt = "SW"
elif wind_deg_dct <= 11:
    wind_deg_lt = "WSW"
elif wind_deg_dct <= 12:
    wind_deg_lt = "W"
elif wind_deg_dct <= 13:
    wind_deg_lt = "WNW"
elif wind_deg_dct <= 14:
    wind_deg_lt = "NW"
else:
    wind_deg_lt = "NNW"

print("Direction: ", wind_deg_lt)
