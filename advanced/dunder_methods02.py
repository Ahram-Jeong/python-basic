# Q : names라는 이름 리스트를 인자로 받는 Students 클래스를 만듭니다.
# 클래스 객체가 보유하고 있는 학생 수를 반환하는 함수와 인스턴스를 출력하려는 경우 발생하는 것을 정의하는 또다른 함수를 구현하세요. 출력할 때 모든 학생의 이름이 표시되어야 합니다.

class Students():
    def __init__(self, names):
        self.names = names

    def __len__(self):
        return len(self.names)

    def __str__(self):
        return f"{self.names}"


tmp = Students(["Woodz", "Ash", "Minhyun"])
print(len(tmp)) # 3
print(tmp) # ['Woodz', 'Ash', 'Minhyun']