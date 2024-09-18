import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print(json)

for people in json['people']:
    print(people['name'])

# print(json)
# {
#     'people': [
#         {'craft': 'ISS', 'name': 'Oleg Kononenko'}, 
#         {'craft': 'ISS', 'name': 'Nikolai Chub'},
#         ...
#     ]
# }