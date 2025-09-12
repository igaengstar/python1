import pandas as pd
df = pd.read_csv('data/score.csv', index_col='지원번호')
search = input('검색할 이름의 일부를 입력하세요: ') 
filt = df['이름'].str.contains(search)
df = df[filt]   
print(df)

if len(df.index) == 0:
    print('검색 결과가 없습니다.')
else:
    print(f'{len(df.index)}명의 학생이 검색되었습니다.')    