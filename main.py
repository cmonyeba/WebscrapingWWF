import requests
import pandas as pd
from pandas import ExcelWriter
from bs4 import BeautifulSoup

page = requests.get('https://www.worldwildlife.org/species/directory?direction=desc&sort=extinction_status')
soup = BeautifulSoup(page.content, 'html.parser')


table = soup.find(class_='lead gutter-bottom-2 table-to-list')
body = table.find("tbody")
contents = body.find_all("tr")
row = contents[0].find_all("td")

#print(row[0].get_text())
#print(row[1].get_text())
#print(row[2].get_text())
   
rows = [content.find_all("td") for content in contents]

#print(rows)

common_name = [row[0].get_text() for row in rows]
scientific_name = [row[1].get_text() for row in rows]
status = [row[2].get_text() for row in rows]

#print(common_name)
#print(scientific_name)
#print(status)

df = pd.DataFrame({'Common Name': common_name, 'Scientific Name': scientific_name, 'Conservation Status': status})

#print(df)

df.to_excel("endangeredspecies.xlsx", sheet_name='data') 