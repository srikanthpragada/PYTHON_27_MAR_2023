import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

for c in countries:
    print(c["name"]["common"])
