import json

x = '{ "name":"Yernar", "age":17, "city":"Almaty"}'
y = json.loads(x)

print(y["city"])
