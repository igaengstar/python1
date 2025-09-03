-- SQLite
-- juso 테이블 데이터 확인
SELECT * FROM juso;

-- product 테이블이 없으면 새로 생성
DROP TABLE IF EXISTS product;

CREATE TABLE product (
    code   INTEGER PRIMARY KEY AUTOINCREMENT,
    name   TEXT NOT NULL,
    price  INTEGER DEFAULT 0 );

INSERT INTO product (name, price) VALUES ('LG 세탁기', 2500000);
INSERT INTO product (name, price) VALUES ('LG 냉장고', 3500000);

SELECT * FROM product;