# Ex1
customer = "조승연"
index = 5
while index >= 1 :
    print(f"{customer} 고객님, 커피가 준비되었습니다. {index}번 동안 무응답 시 순서가 넘어갑니다.")
    index -= 1
    if index == 0 :
        print("다음 고객님의 순서로 넘어갑니다.")

# Ex2
# 무한 루프..
# customer = "황민현"
# index = 0
# while True :
#     print(f"{customer} 고객님, 커피가 준비되었습니다. 호출 {index}회")
#     index += 1

# Ex3
guest = "우즈"
person = "Unknown"

while person != guest :
    print(f"{guest} 고객님, 커피가 준비되었습니다.")
    person = input("성함을 말씀해 주세요. >> ") # 입력한 이름과 일치 시에만 반복문 탈출
