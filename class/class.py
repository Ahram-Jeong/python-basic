class Unit :
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 : {self.hp}, 공격력 : {self.damage}")

# 클래스를 통해 객체 생성 시, __init__ 함수 내의 매개변수를(self 제외) 필수 인자로 넣어 주어야 한다.
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)