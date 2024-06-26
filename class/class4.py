# 일반 유닛
class Unit :
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location) :
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 : {self.speed}]")

# 공격 유닛
class AttackUnit(Unit) :
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
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
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    # 메소드 오버라이딩 (Unit의 move 메소드를 오버라이딩 함)
    def move(self, location) :
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 객체 생성
vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# 메소드 호출
vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")