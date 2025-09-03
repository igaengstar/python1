from function import *

file_name = 'data/juso.txt'

def insert(no, name, phone, address):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f"{no}, {name}, {phone}, {address}\n")
    print("등록 완료!")

def read():
    contacts = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) < 4:       # 잘못된 줄 방어
                    continue
                no = parts[0].strip()
                name = parts[1].strip()
                phone = parts[2].strip()
                address = parts[3].strip()
                contacts.append({'no': no, 'name': name, 'phone': phone, 'address': address})
    except FileNotFoundError:
        # 파일이 없으면 빈 목록 반환
        return []
    return contacts

def search(name):
    items = read()
    results = []
    for item in items:
        if item['name'].find(name) != -1:
            results.append(item)
    return results
    
def maxNo():
    items = read()
    nos = []
    for item in items:
        try:
            nos.append(int(item['no']))
        except (ValueError, TypeError):
            continue
    if not nos:
        return 0
    return max(nos)

while True: 
    menuPrint("주소관리")
    menu = input("메뉴선택> ").strip()

    if menu == "0":
        break

    elif menu == "1":  # 등록
        name = input("이름> ").strip()
        if name == "":
            continue
        phone = input("전화> ").strip()
        address = input("주소> ").strip()
        no = maxNo() + 1                   # ← 신규 번호 생성
        insert(no, name, phone, address)

    elif menu == "3":  # 목록
        items = read()
        for item in items:
            print(f"{item.get('no')}, {item.get('name')}, {item.get('phone')}, {item.get('address')}")

    elif menu == "2":  # 검색
        name = input("검색이름> ").strip()  # ← 먼저 입력 받기
        results = search(name)
        if len(results) == 0:
            print(f"'{name}'라는 데이터가 없습니다.")
            continue
        for item in results:
            print(f"{item.get('no')}, {item.get('name')}, {item.get('phone')}, {item.get('address')}")