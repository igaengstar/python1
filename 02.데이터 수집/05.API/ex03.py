import json, os, folium, webbrowser

# 📌 JSON에서 매장 목록 불러오기
def getAddress():
    # data/hollys_location.json 파일을 열고 파이썬 객체(리스트)로 변환
    with open('02.데이터 수집/05.API/data/hollys_location.json', 'r', encoding='utf8') as f:
        return json.load(f)

# 📌 주소 검색 함수
def searchAddress(address):
    stores = getAddress()   # 전체 매장 불러오기
    result = []
    for s in stores:
        # 매장의 주소 안에 검색어가 포함되어 있으면
        if address in s['address']:
            # 매장명, 주소, 전화번호 출력
            print(f"{s['name']}, {s['address']}, {s['phone']}")
            result.append(s)   # 결과 리스트에 추가
    return result

# 📌 지도 생성 함수
def createMap(stores, address):
    # 지도 중심을 첫 번째 매장의 좌표로 설정
    y, x = stores[0]['y'], stores[0]['x']
    fmap = folium.Map((y, x), zoom_start=15, width='100%', height='100%')

    # 검색된 매장마다 지도에 마커 추가
    for s in stores:
        text = f'{s["name"]}<br>{s["phone"]}<br>{s["address"]}'  # 팝업 텍스트
        folium.Marker(
            (s['y'], s['x']),                   # 매장 좌표
            folium.Popup(text, max_width=200),   # 팝업 내용
            icon=folium.Icon(color='blue', icon='road', prefix='fa')  # 아이콘
        ).add_to(fmap)

    # 저장 폴더(data/map)가 없으면 생성
    os.makedirs('data/map', exist_ok=True)

    # 검색어를 파일명으로 해서 HTML 저장
    out_path = f'data/map/{address}.html'
    fmap.save(out_path)
    return out_path   # 저장된 HTML 경로 반환

# 📌 메인 실행부
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')  # 화면 지우기(윈도우/맥/리눅스 호환)
    while True:
        addr = input("\n매장주소> ").strip()  # 검색어 입력
        if addr == '':
            break  # 입력이 없으면 종료

        stores = searchAddress(addr)  # 검색 실행
        if not stores:                # 결과가 없으면
            print('검색한 매장이 없습니다.')
        else:
            sel = input('지도를 출력하실래요(Y)> ').lower()
            if sel == 'y':
                # 지도 생성 → HTML 파일 저장
                html = createMap(stores, addr)
                # 웹브라우저로 HTML 파일 열기
                webbrowser.open('file://' + os.path.abspath(html))
                print('지도를 열었습니다 →', os.path.abspath(html))