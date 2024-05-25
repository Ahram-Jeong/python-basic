# 일반 유닛
class Unit :
    def __init__(self, name, hp) :
        self.name = name
        self.hp = hp
        # self.damage = damage
        # print(f"{self.name} 유닛이 생성되었습니다.")
        # print(f"체력 : {self.hp}, 공격력 : {self.damage}")

# 공격 유닛
class AttackUnit(Unit) :
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
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

# 공중 유닛
class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print(f"{name} : {location} 방향으로 날아갑니다.  [속도 : {self.flying_speed}]")

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# FlyableAttackUnit 객체 생성
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)

# 부모 클래스 Flyable의 fly 메소드 호출
valkyrie.fly(valkyrie.name, "3시")