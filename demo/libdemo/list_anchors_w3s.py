import requests
from bs4 import BeautifulSoup

website = "https://www.w3schools.com"

resp = requests.get(website)
contents = resp.text
bs = BeautifulSoup(contents, 'html.parser')
anchors = bs.find_all("a")
for a in anchors:
    href = a['href']
    if href == '#':
        continue

    if 'javascript:void' in href:
        continue

    if not href.startswith("http"):  # relative url
        if not href.startswith("/"):
            href = "/" + href
        href = website + href  # convert to absolute url

    print(href)
