while True:
    
    try:
        num = input("숫자> ")   # 문자열 입력
        if num == "":break
        num = int(num)          # 정수 변환 시도
    except Exception as err:    # 예외 발생 시
        print("알 수 없는 오류 발생:", err)              # 예외 메시지 출력
