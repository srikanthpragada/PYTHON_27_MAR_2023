import requests
from bs4 import BeautifulSoup

website = "http://www.srikanthtechnologies.com"

resp = requests.get(website)
contents = resp.text
bs = BeautifulSoup(contents, 'html.parser')
anchors = bs.find_all("a")
for a in anchors:
    href = a['href']
    if href == '#':
        continue

    if not href.startswith("http"):  # relative url
        href = website + "/" + href  # convert to absolute url

    print(href)
