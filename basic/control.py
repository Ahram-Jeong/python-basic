password = "mypassword1234"
stored_pw = "mypassword"
admin = True

if password == stored_pw :
    print("passwords match :)")
elif admin :
    print("passwords did not match, but ADMIN granted!")
else :
    print("no password match and not an admin :(")

# Q : a와 b의 합이 42인지 확인하는 제어 흐름 루틴을 작성하세요. 합이 42이라면 42를 출력하세요. 그렇지 않다면 합이 30과 41 사이인지 확인하고, a와 b의 합을 출력하세요. 그것도 아니라면 False를 출력하세요.
a = 23
b = 8
result = a + b

if result == 42 :
    print(42)
elif 30 < result < 41 :
    print(result)
else :
    print("False")