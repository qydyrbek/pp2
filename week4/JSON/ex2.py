import json

x = {
  "name": "Yernar",
  "age": 17,
  "city": "Almaty"
}
y = json.dumps(x)

print(y)
