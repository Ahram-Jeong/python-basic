# Q : 개의 이름, 품종 및 나이를 가진 Dog 클래스를 만드세요. 개의 나이에 7을 곱하여 사람 나이로 계산한 나이를 구하여 결과로 반환하는 calculate_human_age라는 메서드를 정의하세요.
class Dog():
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def calculate_human_age(self):
        return 7 * self.age

dog1 = Dog("Hans", "저먼 셰퍼드", 7)
print(dog1.calculate_human_age()) # 49