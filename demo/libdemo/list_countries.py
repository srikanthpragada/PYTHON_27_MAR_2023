import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

for c in sorted(countries, key=lambda c: c['name']['common']):
    print(c["name"]["common"])
