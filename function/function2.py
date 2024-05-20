def profile(name, age, main_lang) :
    print(f"이름 : {name}\t나이 : {age}세\t주 사용 언어{main_lang}")

profile("조승연", 28, "자바")
profile("황민현", 27, "파이썬")

# 매개변수에 기본 값 설정
def profile2(name, age = 8, main_lang = "Python") :
    print(f"이름 : {name}\t나이 : {age}세\t주 사용 언어{main_lang}")

profile2("김루이")
profile2("김로미")