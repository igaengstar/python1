import os
import sqlite3

path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/haksa.db'

con = sqlite3.connect(db_name)
cur = con.cursor()

class Dept:
    def __init__(self):
        self.code = 0
        self.dname = ''   # 학과명 필드는 dname 으로 사용

class Student(Dept):  #**
    def __init__(self):
        super().__init__()  #상속받음
        self.id = ''
        self.name = ''
        self.dept = 0       # 소속 학과 코드

    def print(self):
        print(f'학번: {self.id}, 이름: {self.name}, 학과: {self.dname}({self.dept})')

def listDept():
    try:
        sql = 'select * from dept'
        cur.execute(sql)
        rows = cur.fetchall()
        list =[]
        for row in rows:
            dept = Dept()
            dept.code = row[0]
            # FIX: Dept에는 name 속성이 없고 dname 을 쓰므로 dname 에 대입
            dept.dname = row[1]
            list.append(dept)
        return list
    except Exception as err:
        print('학과목록:', err)

def list():
    """학과 목록(dept) 반환"""
    try:
        sql = 'select * from dept'
        cur.execute(sql)
        rows = cur.fetchall()
        list = []
        for row in rows:
            dept = Dept()
            dept.code = row[0]
            dept.dname = row[1]   # 일관되게 dname 사용
            list.append(dept)
        return list
    except Exception as err:
        print('목록 에러:', err)

def list_students():
    """FIX: 학생 목록을 불러오는 별도 이름 제공 (main에서 list()와 혼동 방지)"""
    try:
        sql = 'select id, dept, name, dname from vstudent order by id'
        cur.execute(sql)
        rows = cur.fetchall()
        res = []
        for row in rows:
            stu = Student()
            stu.id, stu.dept, stu.name, stu.dname = row
            res.append(stu)
        return res
    except Exception as err:
        print('학생목록 에러:', err)
        return []

def search(value):  #검색
    try:
        sql = 'select * from vstudent where (name like ? or id like ? or dname like ?)'
        value = f'%{value}%'
        cur.execute(sql, (value, value, value,))
        rows = cur.fetchall()
        list = []
        for row in rows:
            stu = Student()
            stu.id = row[0]
            # FIX: vstudent 의 2번째 컬럼은 dept(학과코드)이므로 stu.dept 에 대입
            stu.dept = row[1]
            stu.name = row[2]
            stu.dname = row[3]
            list.append(stu)
        return list
    except Exception as err:
        print('검색오류:', err)
        return []   # FIX: 실패 시 빈 리스트 반환(상위 len/반복 안전)

def newID():
    try:
        sql = 'select max(id)+1 from student'
        cur.execute(sql)
        row = cur.fetchone()
        new_id = row[0]
        return new_id
    except Exception as err:
        print('코드생성:', err)

def insert(stu):  #등록
    try:
        sql = 'insert into student(id, name, dept) values(?, ?, ?)'
        cur.execute(sql, (stu.id, stu.name, stu.dept,))
        con.commit()
    except Exception as err:
        print('입력오류:', err)

def inputDept():
    depts = listDept()
    for dept in depts:
        print(f'{dept.code}.{dept.dname}', end='|')  # dname 으로 일관
    print()
    codes = [dept.code for dept in depts]

    while True:
        code = input('학과코드>')
        if code == '':
            print('학과코드는 반드시 입력하세요.')
            continue
        elif not code.isnumeric():
            print('학과코드는 숫자로 입력하세요.')
        elif codes.count(int(code)) == 0:
            print(f'{min(codes)}~{max(codes)}번을 입력하세요.')
        else:
            return int(code)

def read(id):
    try:
        sql = 'select id, name, dept, dname from vstudent where id=?'
        cur.execute(sql, (id,))
        row = cur.fetchone()
        # FIX: 조회 결과가 없을 수도 있으므로 None 방어
        if row is None:
            return None
        stu = Student()
        stu.id, stu.name, stu.dept, stu.dname = row
        return stu
    except Exception as err:
        print('학번읽기오류:', err)

def delete(id):
    """FIX: 학생 삭제 구현"""
    try:
        sql = 'delete from student where id=?'
        cur.execute(sql, (id,))
        con.commit()
        return cur.rowcount   # 0이면 없음, 1이면 삭제됨
    except Exception as err:
        print('삭제오류:', err)
        return 0
    
def update(stu):
    try:
        sql = 'UPDATE student SET name=?, dept=? WHERE id=?'
        cur.execute(sql, (stu.name, stu.dept, stu.id))
        con.commit()
        return cur.rowcount   # 몇 건 수정되었는지 반환
    except Exception as err:
        print('학생수정오류:', err)
        return 0

if __name__=='__main__':
    stu = read('2501')
    if stu is None:
        print('학생이 없습니다.')
    else:
        stu.print()