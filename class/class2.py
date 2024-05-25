class Unit :
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 : {self.hp}, 공격력 : {self.damage}")

class AttackUnit :
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location) :
        # 전달받은 parameter를 그대로 사용할 땐 self 없이 사용
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 : {self.damage}]")

    def damaged(self, damage) :
        self.hp -= damage
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0 :
            print(f"{self.name} : 파괴되었습니다.")

# AttackUnit 객체 생성
firebat1 = AttackUnit("파이어뱃", 50, 16)

# attack 함수 호출
firebat1.attack("5시")

# damaged 함수 호출
firebat1.damaged(25)
firebat1.damaged(25)