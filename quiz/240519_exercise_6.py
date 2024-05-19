# for문을 이용하여 다음 리스트에 들어있는 요소 중 가장 큰 수를 찾아 출력하시오.
list = [4, 5, 2, 1, 99, 15, 2, 7, 27]
tmp = list[0]  # 비교 리스트의 첫 번째 값

for i in list:
    if i > tmp:
        tmp = i

print(tmp) # 99

# for문을 이용하여 다음 리스트에 들어있는 요소 중 가장 작은 수를 찾아 출력하시오.
list2 = [4, 5, 2, 1, 99, 15, 2, 7, 27]
tmp2 = list2[0]  # 비교 리스트의 첫 번째 값

for i in list2:
    if i < tmp2:
        tmp2 = i

print(tmp2) # 1

# 1부터 100사이의 숫자 중 3의 배수인 값들의 합을 출력하시오.
# 정답 : 1683
sum = 0

for i in range(3, 101, 3):
    sum += i

print(sum)

# for문을 이용하여 구구단 2단을 출력하시오.
for j in range(1, 10) :
    print(f"2 * {j} = {2*j}")

# 숫자를 입력 받고 입력 받은 숫자의 약수를 구하시오.
# 약수란 어떤 수를 나누어 떨어지게 하는 수 (나누었을 때 나머지가 0)

# 출력 예시
# 정수 입력 >>  32
# 32의 약수 : 1 2 4 8 16 32
num = int(input("정수 입력 >> "))

print(f"{num}의 약수 : ", end = "")

for i in range(1, num+1) :
    if num % i == 0 :
        print(i, end = " ")
