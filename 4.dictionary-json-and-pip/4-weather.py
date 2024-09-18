import requests

location = 'Vietnam'
url = f'http://api.weatherapi.com/v1/current.json?key=befae6ee916f446aa5f114814240309&q={location}&aqi=no'
response = requests.get(url)
json = response.json()

temp_c = json.get('current').get('temp_c')
condition = json.get('current').get('condition').get('text')

print('Weather in',location, 'is', condition, 'and', temp_c, 'degrees')  