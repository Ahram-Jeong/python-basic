# 초를 정수로 입력 받아 “00시간 00분 00초” 형태로 출력하시오.
# 1시간 = 60분 = 3600초
time = int(input("초 입력 >> "))
hour = time // (60**2)
min = time % (60**2) // 60
sec = time % 60 % 60

print(f"{hour}시간 {min}분 {sec}초")

# 지수 연산자
num =  int(input("정수 입력 >> "))
pow =  int(input("지수 입력 >> "))
print(f"{num}의 {pow}승은 {num**pow}입니다.")

# Random 라이브러리를 import하여 2개의 난수를 각각 변수에 담아주고
# 비교연산자를 이용하여 출력 값을 확인하시오.
import random
a = random.randint(1, 10)
b = random.randint(1, 10)
print(f"a : {a}, b : {b}")
print(a < b)
print(a > b)
print(a == b)
print(a != b)

# 삼항연산자
# (참일 때 코드) if 조건식 else (거짓일 때 코드)

# 두 개의 정수를 입력 받아 큰 수를 출력하시오
a = int(input("정수 입력 >> "))
b = int(input("정수 입력 >> "))
print(f"a : {a}" if a > b else f"b : {b}")

# 두 개의 정수를 입력 받아 큰 수에서 작은 수를 뺀 결과 값을 출력하시오.
a = int(input("첫 번째 정수 입력 >> "))
b = int(input("두 번째 정수 입력 >> "))
print(f"두 수의 차 : {a-b}" if a > b else f"두 수의 차 : {b-a}")

# 정수를 입력 받아 홀수인지 짝수인지를 판별하시오.
num = int(input("정수 입력 >> "))
print(f"{num}은 짝수입니다." if (num % 2 == 0) else f"{num}은 홀수입니다.")