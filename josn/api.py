
import requests         #=> to send order to web
import json             #= >to read josn data which requests will return

# divided url to three section 

# section three
my_api_key = '630ed580d7a01807beccfb2993f239e2'

# if you need to transform temp  =>    put this after api key   '&units=metric'

# section one
base_url = 'https://api.openweathermap.org/data/2.5/weather?'

# section two
city_name = input('entre your city name')

# q={city name}&appid={API key}

compelet_url = base_url + 'q=' + city_name + '&appid=' + my_api_key

# response object
response = requests.get(compelet_url)     #=> will bring data from this url and store in the variable "response"
# print(response.text)

# read josn data and convert to dict python
x = json.loads(response.text)

"""if cod at the end in the coordinate  == 200
    then the order sent successfuly but it was  == 404
    then it cannot find the city"""

if x['cod'] != '404':
    y = x['main']                  #=> main countain data that i need
    humidity = y['humidity']
    temp =y['temp']
    z = x['weather'][0]['description']
    print(f'temperture is  => {humidity} and {temp}')
    print(z)

else :
    print('the city not found')