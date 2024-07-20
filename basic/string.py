myvar = "Hello WOODZ how is your dog"
print(myvar.upper())
print(myvar.split())
print(myvar[-1])
print(myvar[0:5])

first_name = "WOODZ"
last_name = "Cho"
print(f"Hello {last_name} {first_name}")
print(f"Last name is {last_name}")

# Q : "I love programming with python!" 이라는 문자열의 두 번째 단어를 모두 대문자로 출력하세요.
# A : I LOVE programming with python!
input_string = "I love programming with python!"
tmp = input_string.split()

for i in range(len(tmp)) :
    if tmp[1] :
        tmp[1] = tmp[1].upper()
    print(tmp[i], end = " ")