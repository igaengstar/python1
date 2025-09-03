import requests  #웹상의 데이터를 가져옴
import os

path = os.getcwd() + '/data'  #= f'{os.getcwd}/data'
if not os.path.exists(path):
    os.makedirs(path)  #make directories

name = input('이름> ')

#ctrl + click
#q에 검색 매개변수 있음
url = f'https://www.google.com/search?sca_esv=5d812c3a7137edf1&udm=2&fbs=AIIjpHyDg0Pef0CibV20xjIa-FRejxCuOmkq074km2sZXr7uq8hqY3b-NkqmHBgKS9xzRFsJd68YxnQqXZ0YI1vLWbx74P-HB5jYNR9ehU8zZhY1pWhcvPw7aR-heDa0orPab1S7FkaxTeoOJQ-bdUK2P2UhelO3VGOsjmFEm5l8pyPoWGZTbyLKn-dLkbmTsgh1e_VL_IAgzzkB9YlnpiGCSOhT1vQpmCZb7SHxLWGfVHNWsmV55x0&q={name}&sa=X&sqi=2&ved=2ahUKEwi59fKp67iPAxWir1YBHcICL-AQtKgLegQIGBAB&biw=1536&bih=695&dpr=1.25'
params = {'q': name}
res = requests.get(url)

#print(res) <Response [200]> /200=성공
file_name =f'data/{name}.html'
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(res.text)
