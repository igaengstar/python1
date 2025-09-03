import os, requests
from bs4 import BeautifulSoup

os.system('clear')
#[네이버]-[네이버 증권]-[Top 종목]-[거래상위] 목록을 출력
url = 'https://finance.naver.com/'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')
items = soup.find('tbody', attrs={'id':'nxt_topItems1'})

ranks = items.find_all('tr')
print(5, len(ranks))

for index, rank in enumerate(ranks):
    td = rank.find_all('td')
    price = td[0].get_text()
    up_down=td[2].get_text().strip()
    print(index+1, rank.a.get_text(), price, up_down)


