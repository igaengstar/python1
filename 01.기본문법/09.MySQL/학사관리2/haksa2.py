import pymysql

# -------------------------------
# 전역 DB 연결
# -------------------------------
con = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='haksa',
    charset='utf8mb4',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)
cur = con.cursor()

# -------------------------------
# 학과 클래스
# -------------------------------
class Dept:
    def __init__(self):
        self.dcode = 0
        self.dname = ''

# -------------------------------
# 학생 클래스
# -------------------------------
class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.code = 0
 
    def print(self):
        print(f'학번:{self.id}, 이름:{self.name}, 학과:{self.dname}({self.code})')
        print('-' * 50)

# -------------------------------
# 학생 목록 조회
# -------------------------------
def list_students(key):
    try:
        keys = ['id', 'name', 'dname']
        sql = f'SELECT * FROM vstudent ORDER BY {keys[key-1]}'
        cur.execute(sql)
        rows = cur.fetchall()

        result = []
        for row in rows:
            stu = Student()
            stu.id = row['id']
            stu.name = row['name']
            stu.dname = row['dname']
            stu.code = row['code']
            result.append(stu)
        return result
    except Exception as err:
        print('학생목록 오류:', err)
        return []

# -------------------------------
# 학생 검색
# -------------------------------
def search(value):
    try:
        sql = '''
        SELECT * FROM vstudent
        WHERE id LIKE %s OR name LIKE %s OR dname LIKE %s
        '''
        value = f'%{value}%'
        cur.execute(sql, (value, value, value))
        rows = cur.fetchall()

        result = []
        for row in rows:
            stu = Student()
            stu.id = row['id']
            stu.name = row['name']
            stu.dname = row['dname']
            stu.code = row['code']
            result.append(stu)
        return result
    except Exception as err:
        print('학생검색 오류:', err)
        return []

# -------------------------------
# 학번 생성
# -------------------------------

def newID():
    try:
        sql = 'SELECT LPAD(COALESCE(MAX(id), 0) + 1, 4, "0") AS new_id FROM student'
        cur.execute(sql)
        row = cur.fetchone()
        return row['new_id']
    except Exception as err:
        print('새로운 학번 오류:', err)
        return None

# -------------------------------
# 학과 목록 조회
# -------------------------------
def listDept():
    try:
        sql = 'SELECT * FROM dept'
        cur.execute(sql)
        rows = cur.fetchall()

        result = []
        for row in rows:
            dept = Dept()
            dept.dcode = row['dcode']
            dept.dname = row['dname']
            result.append(dept)
        return result
    except Exception as err:
        print('학과목록 오류:', err)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

# -------------------------------
# 학과 코드 입력                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             --------------
# ------------------------------- 
def inputCode(title, menu):
    depts = listDept()                      # 변수명 변경(내장 list 가리지 않음)
    codes = [d.dcode for d in depts]        # 정수 코드 목록

    print('-' * 50)
    for d in depts:                         # 모든 학과를 먼저 보여주고
        print(f'{d.dcode}.{d.dname}', end='|')
    print()                                 # 한 줄 개행
    print('-' * 50)

    while True:                             # 그 다음 한 번만 입력 루프
        code = input(title)
        if code == '':
            print('학과 코드는 꼭 입력하세요!')
        elif not code.isnumeric():
            print('학과는 숫자로 입력하세요!')
        elif int(code) not in codes:
            print(f'{codes} 코드번호를 입력하세요!')
        else:
            return int(code)
# -------------------------------      
#학생 입력 
# -------------------------------
def insert(stu):
    try:
        sql = 'insert into student(id, name, code) values(%s, %s, %s)'
        cur.execute(sql, (stu.id, stu.name, stu.code))
        con.commit()
        print('학생등록완료!')
    except Exception as err:
        print('학생등록 오류:', err)

# -------------------------------
#학생 읽기
# -------------------------------
def read(id):
    try:
        sql = 'select * from vstudent where id = %s'
        cur.execute(sql, (id,))          # ← 쉼표로 튜플
        row = cur.fetchone()
        if row is None:
            return None
        stu = Student()
        stu.id = row['id']
        stu.name = row['name']
        stu.dname = row['dname']
        stu.code = row['code']
        return stu
    except Exception as err:
        print('학생읽기오류', err)
        return None

# -------------------------------
#학생 삭제 함수
# -------------------------------
def delete(id):
    try:
        sql = 'delete from student where id = %s'
        cur.execute(sql, (id))
        con.commit()
        print('학생삭제완료!')
    except Exception as err:
        print('학생삭제오류:', err)

# -------------------------------
# 학생 수정 함수
# -------------------------------  
def update(stu):
    try:
        sql = 'UPDATE student SET name = %s, code = %s WHERE id = %s'
        cur.execute(sql, (stu.name, stu.code, stu.id))
        con.commit()
        print('학생수정 완료!')
    except Exception as err:
        print('학생수정 오류!', err)


# -------------------------------
# 학과 등록 함수
# -------------------------------  
def insertDept(dname):
    sql = 'INSERT into dept(dname) values(%s)'
    cur.execute(sql, (dname))
    con.commit()
    print('학과등록 완료!')

# -------------------------------
# 학과 읽기
# -------------------------------
def readDept(dcode):
    sql = 'SELECT * FROM dept WHERE dcode = %s'
    cur.execute(sql, (dcode))
    row = cur.fetchone()
    dept = Dept()
    dept.dcode = row['dcode']
    dept.dname = row['dname']
    return dept


# -------------------------------
#학과 수정
# -------------------------------
def updateDept(dept):
    sql = 'UPDATE dept SET dname = %s WHERE dcode = %s'
    cur.execute(sql, (dept.dname, dept.dcode))
    con.commit()
    print('학과수정 완료!')


# -------------------------------
# 실행부
# -------------------------------
if __name__=='__main__':
    id = input('학번>')
    stu = read(id)
    if stu==None:
        print('학생이 없습니다.')
    else:
        stu.print()


