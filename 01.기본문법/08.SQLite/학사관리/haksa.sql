-- SQLite
-- 🔄 기존 테이블 있으면 삭제
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS dept;


-- 🏫 학과 테이블
CREATE TABLE dept(
    code INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR
(200)
);

-- 👨‍🎓 학생 테이블
CREATE TABLE student
(
    id CHAR(4) PRIMARY KEY NOT NULL,
    dept INTEGER NOT NULL,
    name CHAR(50) NOT NULL,
    FOREIGN KEY(dept) REFERENCES dept(code)
);

-- 📥 학과 데이터 삽입
INSERT INTO dept
    (name)
VALUES
    ('컴퓨터공학과');
INSERT INTO dept
    (name)
VALUES
    ('전자공학과');
INSERT INTO dept
    (name)
VALUES
    ('건축공학과');
    INSERT INTO dept
    (name)
VALUES
    ('인공지능학과');

-- 📥 학생 데이터 삽입
INSERT INTO student
    (id, dept, name)
VALUES
    ('2501', 1, '홍길동');
INSERT INTO student
    (id, dept, name)
VALUES
    ('2502', 2, '심청이');
INSERT INTO student
    (id, dept, name)
VALUES
    ('2503', 3, '강감찬');
INSERT INTO student
    (id, dept, name)
VALUES
    ('2504', 4, '이순신');

-- 조인 조회
SELECT s.*, dept.name AS dname FROM student s, dept WHERE s.dept = dept.code;

-- 뷰 생성 (중복 생성 방지)
CREATE VIEW IF NOT EXISTS vstudent AS
SELECT s.*, d.name AS dname
FROM student AS s
JOIN dept    AS d ON s.dept = d.code;

-- 뷰 확인
SELECT * FROM vstudent;

