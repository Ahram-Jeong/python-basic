class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print("Hello:)")

    def report(self):
        print(f"I am {self.first_name} {self.last_name}")

class Agent(Person):
    def __init__(self, first_name, last_name, code_name):
        Person.__init__(self, first_name, last_name)
        self.code_name = code_name

    # Method Overriding
    # 자식 클래스에서 부모 클래스에 이미 정의된 메소드를 재정의하는 것
    def report(self):
        print("I am here.")

    def reveal(self, passcode):
        if passcode == 123:
            print("I am a secret agent:-)")
        else:
            self.report()

x = Person("Minhyun", "Hwang")
x.report()

y = Agent("WOODZ", "Cho", "mr.X")
y.hello()
y.report() # I am here.
y.reveal(123) # I am a secret agent:-)
y.reveal(000) # I am here.
print(y.first_name, y.code_name)