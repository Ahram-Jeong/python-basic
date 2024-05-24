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

# Wraith : 공중 유닛, 비행기 + 클로킹
wraith1 = Unit("레이스", 80, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

wraith2 = Unit("빼앗은 레이스", 80, 5)
# 파이썬은 클래스 외부에서 원하는 변수를 확장할 수 있음
# 확장된 변수는 확장을 한 객체에서만! 적용 됨
wraith2.clocking = True

if wraith2.clocking == True :
    print(f"현재 {wraith2.name}는 클로킹 상태입니다.")

