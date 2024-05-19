# Up, Down 게임
# 1. 랜덤으로 생성된 1 ~ 50 사이의 숫자를 맞추는 게임
# 2. 숫자를 맞추면 “정답을 맞추셨습니다.”를 문구를 출력하고 입력을 중지

# 출력 예시
# 숫자 입력 >>  10
# 10보다 큰 수 입니다.
# 숫자 입력 >>  40
# 40보다 큰 수 입니다.
# 숫자 입력 >>  48
# 48보다 큰 수 입니다.
# 숫자 입력 >>  49
# 정답😇

import random

num = random.randint(1, 50) # randint -> 1 <= x <= 50
user = 0

while not num == user :
    user = int(input("숫자 입력 >> "))
    if num > user :
        print(f"{user}보다 큰 수 입니다.")
    elif num < user :
        print(f"{user}보다 작은 수 입니다.")

print("정답😇")