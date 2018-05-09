import json

a = {1:'liz',2:'emily'}

with open('name.json','w') as wj:
	json.dump(a,wj)

print("Operation Successful")