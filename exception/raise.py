try :
    print("한 자리 정수 나누기 전용 계산기")
    num1 = int(input("첫 번째 정수 입력 >> "))
    num2 = int(input("두 번째 정수 입력 >> "))
    if num1 >= 10 or num2 >= 10 :
        raise ValueError
    print(f"{num1} / {num2} = {num1 / num2}")
except ValueError :
    print("잘못된 값 입력! 한 자리 정수만 입력하세요.")