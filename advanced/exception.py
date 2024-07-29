try :
    print("10" + 10)
except IOError :
    print("You have an input/output error:(")
except TypeError :
    print("You are using the wrong data types:(")
except :
    print("You got an error")
finally :
    print("FINALLY WILL ALWAYS RUN, ERROR OR NO ERROR!")

# Q : 두 값, a와 b를 받아들이고, a / b의 결과를 반환하는 divider(a,b)라는 함수를 작성하세요. b가 0일 때, Python은 예외를 던집니다. 이 ZeroDivisionError가 발생하면, "Please do not divide by zero!"를 출력하는 오류 처리 루틴을 작성하세요.
def divider(a, b):
    try :
        return a / b
    except ZeroDivisionError :
        print("Please do not divide by zero!")