# 숫자 1, 2, 3, 4 에 + 100을 하기로 함 -> 101, 102, 103, 104
num = [1, 2, 3, 4, 5]
print(num)
num = [i + 100 for i in num]
print(num)

# 문자열을 길이로 변환
names = ["명창 고양이", "우즈", "조승연"]
names = [len(i) for i in names]
print(names) # [6, 2, 3]

# 문자열을 대문자로 변환
fruits = ["apple", "cherry", "mango", "orange"]
fruits = [i.upper() for i in fruits]
print(fruits)