import requests
from bs4 import BeautifulSoup

website = "http://www.srikanthtechnologies.com"
resp = requests.get(website)
contents = resp.text
bs = BeautifulSoup(contents, 'html.parser')
# Look for table with schedule
table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    course = cols[1].text  # course
    stdate = cols[3].text  # starting date
    print(f"{course:40}  {stdate:5}")
