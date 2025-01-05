import json

with open("./token.json", 'r') as file:
    data = json.load(file)
api_key = data.get('model_api_key')
print(api_key)