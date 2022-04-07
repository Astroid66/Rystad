import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.eia.gov/dnav/pet/pet_pnp_inpt_a_epc0_yir_mbblpd_m.htm'
page = requests.get(url)


soup = BeautifulSoup(page.text, 'lxml')
table1 = soup.find("table", {"class":"data1"})


headers = []
for i in table1.find_all("th",{"class":"Series5"}):
 title = i.text
 headers.append(title)
headers.insert(0, 'Area')
headers.remove('Sep-21')


print(headers)df = pd.DataFrame(columns = headers)
df.head()

for j in table1.find_all("tr",{"class":"DataRow"})[1:]:
 row_data1 = j.find_all("td",{"class":"DataStub"})
 row_data2 = j.find_all("td",{"class":"DataB"})
 row_data2.pop(1)
 row_data3 = j.find_all("td",{"class":"Current2"})
 row_data4 = j.find_all("td",{"class":"DataHist"})
 row1 = [i.text for i in row_data1]
 row2 = [i.text for i in row_data2]
 row3 = [i.text for i in row_data3]
 url = result.find('a')['href']
 
 row = row1 +row2+ row3
 length = len(df)
 df.loc[length] = row

df.head()

df.Area = df['Area'].replace('\n', '', regex=True) 
df.head()

df.to_csv('data2.csv',index = False)

