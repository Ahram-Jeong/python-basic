class Student():
    # CLASS OBJECT ATTRIBUTE
    # 클래스 변수
    planet = "Earth"
    def __init__(self, name, gpa): # 기본적으로 사용자가 Student 클래스를 생성할 때 name, gpa를 제공해야 함을 의미
        # ATTRIBUTES
        # 인스턴스 변수
        self.name = name
        self.gpa = gpa

stu1 = Student("WOODZ", 4.0)
stu2 = Student("Ash", 4.5)
print(type(stu1), type(stu2))
print(stu1.name, stu1.gpa)
print(stu1.planet)