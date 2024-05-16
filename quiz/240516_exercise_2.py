text = "My name is AR"
print(text[0])
print(text[8])
print(text[-2])
print(text[:2])
print(text[3:7])
print(text[8:10])
print(text[11:])
print(text[8:13])
print(text[-5:])
print(text)
print(text[:])

str1 = "2024년 5월 15일의 날씨는 비입니다."
print("날짜 : ", str1[:12])
print("날씨 : ", str1[-5])

day = 14
str2 = "오늘은 5월 %d일 입니다." %day
print(str2)

month = 3
day = 14
str3 = "오늘은 %d월 %d일 입니다." %(month, day)
print(str3)

month = 6
day = 14
str4 = "오늘은 {}월 {}일 입니다." .format(month, day)
print(str4)

import datetime
now = datetime.datetime.now()
# print(now)
month = now.month
day = now.day
str5 = f"오늘은 {month}월 {day}일 입니다."
print(str5)
print(f"{now.month}월 {now.day}일")

x = 100
y = 200
add = x + y
print(f"{x}와 {y}의 합은 {add}입니다.")
print("%d와 %d의 합은 %d입니다." %(x, y, add))
print("{}와 {}의 합은 {}입니다." .format(x, y, add))

# count 함수
str6 = "오늘 날씨가 너무 좋아서 여행가고 싶네요"
print(str6.count("")) # 23
print(str6.count("가")) # 2

# join 함수
# join 앞 쪽은 구분자의 위치로 각 문자열들 사이를 구분자로 이어주는 역할
print(" ".join(["오늘만", "하면", "내일","쉰다"])) # 오늘만 하면 내일 쉰다

# strip 함수
str7 = "          noname            "
print(str7.strip()) # noname

# replace 함수
str8 = "noname"
print(str8.replace("no", "yes")) # yesname

# split 함수
str9 = "핀테크, 데이터 분석"
str9.split(", ") # ['핀테크', '데이터 분석']

# 연산자
# / 나누기
# // 몫
# % 나머지
num1 = 10
num2 = 7

print(num1/num2) # 1.4285714285714286
print(num1//num2) # 1
print(num1%num2) # 3

# input을 이용한 연산
py = int(input("파이썬 점수 입력 >> "))
ml = int(input("머신러닝 점수 입력 >> "))
dl = int(input("딥러닝 점수 입력 >> "))

total = [py, ml, dl]

print("합계 : ", sum(total))
# 파이썬에는 평균을 구하는 함수가 없음
print("평균 : ", sum(total)/len(total))

str10 = "우와"
print(str10 * 10)
str11 = "안녕하세요 "
print(str11 * 3)