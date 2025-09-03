import csv
import requests
from bs4 import BeautifulSoup
import re

filename = "data/코스닥거래상위1-100.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

url = ' https://finance.naver.com/sise/sise_quant.naver?sosok=1'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

table = soup.find('table', attrs={'class':'type_2'})
rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    if len(cols) <=1 :
        continue
    data = [re.sub('\t|\n|하락|상승|보합','',col.getText()) for col in cols]
    writer.writerow(data)