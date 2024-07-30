# Q : 이름(name)과 종족(species)을 가진 Animal 클래스를 만드세요.
# 그 클래스에 greet()라는 함수를 만들어 "Hi! My name is {name} and I am a {species}"라는 구문을 출력하세요.
# 그런 다음, 이 클래스를 사용하여 Cat과 Dog 클래스를 만드세요.
# 각 클래스는 이름(name)을 인자로 받으며,이 동물이 일반적으로 내는 소리를 출력하는 sound()라는 메서드를 구현하세요. ("ruff"와 같은 문자열로)
# 힌트 : 각 클래스 안에서 부모 클래스를 초기화하는 것을 잊지마세요.

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")

# Cat 클래스
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "cat")

    def sound(self):
        print("Meow")

# Dog 클래스
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "dog")

    def sound(self):
        print("Woof")