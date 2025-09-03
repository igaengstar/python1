import requests
from bs4 import BeautifulSoup
import csv

f = open('data/할리스.csv', "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
title = ['순번', '매장명', '지역명', '주소', '전화']
writer.writerow(title)

seq = 0

for page in range(1, 11):  # 1~10 페이지 크롤링
    url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store='
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    table = soup.find('table', attrs={'class': 'tb_store'})
    rows = table.find_all('tr')

    for index, row in enumerate(rows):
        if index == 0: continue
        columns = row.find_all('td')
        city = columns[0].getText().strip().replace('.', '')
        name = columns[1].getText().strip().replace('.', '')
        address = columns[3].getText().strip().replace(',', ' ').replace('.', '')
        phone = columns[5].get_text().strip().replace('.', '')

        seq += 1
        data = [seq, name, city, address, phone]
        writer.writerow(data)
        print(seq, name, city, address, phone)