class Unit:
    def __init__(self):
        print("Unit 생성자")

    def move(self):
        print("조승연")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
    def move(self):
        print("우즈")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Flyable.__init__(self)
        
    def move(self):
        # super().move()
        Flyable.move(self)

flyableUnit = FlyableUnit()
flyableUnit.move()

# super의 단점 : 다중 상속 시, 상속받는 클래스들의 메소드 명이 동일할 때 가장 먼저 상속 받는 클래스의 메소드를 호출 하므로
# 이런 경우엔 super 보다는 필요한 클래스와 메소드를 명시하는 것이 좋음