import json

with open('list.json') as f:
    data = json.load(f)

for i in data['list_1500']:
    print(i)
    
print(data)