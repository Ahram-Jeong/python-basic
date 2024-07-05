# Q1. 초 단위의 정수를 입력 받아, 시, 분, 초로 나누어 출력하시오.
"""
/ 나누기
// 몫
% 나머지
"""
time = int(input("초 입력 >> "))
hour = time // (60**2) # 1시간 = 3600초
min = time % (60**2) // 60 # 나머지 초를 60으로 나누어 분 계산
sec = time % 60 # 나머지 초를 계산

print(f"{hour}시간 {min}분 {sec}초")

# Q2. 3개의 정수를 입력 받고, 해당 숫자들을 삼각형을 구성하는 각 변의 길이로 삼을 수 있는지 판단하는 프로그램을 작성하시오.
# 만약 가능 하다면 "Possible", 불가능 하다면 "Impossible"을 출력하시오.
a, b, c = map(int, input("세 개의 정수 입력 >> ").split(" "))

if a + b > c and a + c > b and b + c > a :
    print("Possible")
else :
    print("Impossible")

# Q3. 정수를 입력받아 해당 숫자가 소수인지 판별하는 프로그램을 작성하시오. (소수는 1과 자기 자신으로 밖에 나뉘지 않는 자연수)
num = int(input("정수 입력 >> "))

if num <= 1 :
    print("It is not a Prime Number.")
else :
    is_prime = True # 플래그 변수 생성
    for i in range(2, num) :
        if num % i == 0 : # 2 ~ num-1 의 숫자로 나눴을 때 나머지가 0이 되면
            is_prime = False # 소수가 아님
            break
    if is_prime :
        print("It is a Prime Number.")
    else :
        print("It is not a Prime Number.")