def say_hello(first_name, last_name) :
    return f"Hello {first_name} {last_name}"

tmp = say_hello("WOODZ", "Cho")
print(tmp)

def checker(num) :
    if num > 100 :
        return "greater than 100"
    else :
        return "not greater than 100"

print(checker(900))

mylist = [1, 2, 3, 4, 5, 7, 3, 4, 6, 8, 9]
def check_num(list_to_check) :
    for num in list_to_check :
        if num == 10 :
            return True
    return False # 주의 : return False를 else 안에서 처리해 버리면 첫번 째 for loop에서 멈추게 됨!

print(check_num(mylist)) # False

# Q : 두 값, a와 b를 "+" 또는 "-" 문자열 연산자를 허용하는 calculator라는 함수를 구현하세요. 함수는 'a 연산자 b'를 결과로 반환해야 합니다. (즉, a+b 또는 a-b)
def calculator(a, b, operator) :
    if operator == "-" :
        return a - b
    elif operator == "+" :
        return a + b