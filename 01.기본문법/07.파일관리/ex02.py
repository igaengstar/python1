file_name = "data/juso.txt"

try:

    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        #print(lines, type(lines), len(lines))
        for line in lines:
            #print(line, end='')
            items = line.split(",")
            print(f"이름:{items[0]}, 전화:{items[1]}, 주소:{items[2]}", end="")

except Exception as err:
    print("주소 파일을 찾을 수 없습니다")