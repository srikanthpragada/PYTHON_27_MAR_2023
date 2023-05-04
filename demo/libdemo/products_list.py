import json

with open("products.json", "rt") as f:
    products = json.load(f)

for p in products:
    print(f"{p['name']:30}  {p['price']:10}")
