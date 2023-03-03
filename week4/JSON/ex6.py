import json

x = {
  "name": "Yernar",
  "age": 17,
  "married": False,
  "divorced": False,
  "children": ("no children"),
  "pets": None,
  "cars": [
    {"model": "BMW i8", "mpg": 27.5},
    {"model": "Lexus NX250", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = ")))