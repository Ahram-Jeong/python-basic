# Q : 개의 이름과 품종을 갖는 Dog 클래스를 만드세요. 이 클래스를 사용하여 "Hans"라는 "저먼 셰퍼드"종과 "Lou"라는 "레브라도"종의 두 마리의 Dog 객체를 만드세요. 마지막으로 f-string을 사용하여 "Hans and Lou are friends”라는 문구 내에 두 마리 개의 이름을 출력하세요. (var.name과 같이 속성 호출을 사용)
class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Hans", "저먼 셰퍼드")
dog2 = Dog("Lou", "레브라도")

print(f"{dog1.name} and {dog2.name} are friends")