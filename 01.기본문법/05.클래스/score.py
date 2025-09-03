from student import Student

class Score(Student):
    def __init__(self):  # 성적(객체)를 생성하는 생성자
        super().__init__()   # Student의 no, name, dept, birthday 초기화
        self.kor = 0
        self.eng = 0
        self.mat = 0

    def info_print(self):
        super().info_print()  # 번호/성명/학과/생일 출력
        print(f"국어:{self.kor}, 영어:{self.eng}, 수학:{self.mat}")

    def average(self) -> float:
        """과목 평균 반환"""
        return (self.kor + self.eng + self.mat) / 3

    def result(self) -> str:  # 결과 구하는 메서드(함수)
        avg = self.average()
        return "Fail" if avg < 70 else "Success"

    def to_dict(self) -> dict:  # 딕셔너리로 변환하는 메서드(내장 dict와 충돌 피함)
        avg = self.average()
        return {
            'no': self.no,
            'name': self.name,
            'kor': self.kor,
            'eng': self.eng,
            'mat': self.mat,
            'avg': avg,
            'result': self.result()
        }

if __name__ == '__main__':
    s = Score()
    s.no = '01'
    s.name = '홍길동'
    s.kor = 96
    s.mat = 80
    s.eng = 50
    s.info_print()
    d = s.to_dict()
    # 보기 좋게 출력
    print(f"평균: {d['avg']:.2f}, 결과: {d['result']}")
    print(d)