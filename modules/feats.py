from bs4 import BeautifulSoup

import requests

url = "https://www.13thagesrd.com/feats/"

r = requests.get(url)

data = r.text
soup = BeautifulSoup(data, features="html.parser")

tables = soup.find_all('table')

for table in tables:
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    output = []

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        output.append([ele for ele in cols if ele])

    for o in output:
        print (o)
