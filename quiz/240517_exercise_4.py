# 주민등록번호 뒷 자리를 입력 받아 성별을 구분하는 코드를 작성하시오.
# 1. str -> 인덱싱 처리
num = input("주민등록번호 뒷자리를 입력하세요 >> ")

if num[0] == "1" or num[0] == "3" :
    print("성별 : 남자")
elif num[0] == "2" or num[0] == "4" :
    print("성별 : 여자")

# 2. int 형으로 처리
num = int(input("주민등록번호 뒷자리를 입력하세요 >> "))
gen = num // 1000000 # 몫을 구하는 연산자

if gen == 1 or gen == 3 :
    print("성별 : 남자")
elif gen == 2 or gen == 4 :
    print("성별 : 여자")

# 나이, 신용카드 소지 여부를 입력 받아 놀이동산 입장을 예약하는 프로그램을 만들어보세요.
# 성인 기본 요금은 35,000원이고, 미성년자는 성인의 50% 가격이 기본 요금 입니다.
# (조건 : 성인 기준은 19살 이상, 신용카드 추가 할인율은 성인 30%, 미성년자 10%)
name = input("이름 입력하세요 >> ")
age = int(input("나이를 입력하세요 >> "))
card = input("카드 소지 여부 (Y, N) >> ")
price = 35000

if age < 19 :
    price *= 0.5
    if card == "Y" :
        price *= 0.9
elif age >= 19 and card == "Y" :
    price *= 0.7

print(f"{name}님은 입장료 {int(price)}원에 예약되셨습니다.")

# 마스크를 대량 구매하여 주변 친구들에게 소분해서 나눠 주기 위해 포장지를 사려고 합니다.
# 포장지는 8개들이와 5개들이 2종류가 있습니다.
# 8개들이 포장지는 비싸기 때문에 반드시 전부 채워서 포장할 때만 사용하고, 나머지는 5개들이로 포장합니다.
# 과연 포장지는 각각 몇 개가 필요할까요?
# (단, 남는 마스크 없이 전부 포장해야 하며, 마스크는 최소 1개 이상이 있음)
# 풀이 1.
import math

countOfMask = int(input("마스크 개수 입력 >> "))
eightMask = 0 # 8개 번들 개수
fiveMask = 0 # 5개 번들 개수
left = 0 # 입력 값이 8 미만일 때

if countOfMask >= 8 :
    eightMask = countOfMask // 8
    fiveMask = countOfMask % 8 / 5
    print(f"8개 번들 : {eightMask}개 \n5개 번들 : {math.ceil(fiveMask)}개")
else :
    left = countOfMask / 5
    # 1 ~ 5개 -> 1 set
    # 5개 < left < 8개 -> 2 set
    print(f"5개 번들 : {math.ceil(left)}개")

# 풀이 2.
countOfMask = int(input("마스크 개수 입력 >> "))

mask8 = countOfMask // 8
mask5 = countOfMask % 8 // 5

# 8개 번들과 5개 번들로 포장 후 나머지
# 남은 마스크의 개수가 1 ~ 4인 경우
if countOfMask % 8 % 5 >= 1 :
    mask5 += 1 # 5개 번들 포장지 +1

print(f"8개 번들 : {mask8}개")
print(f"5개 번들 : {mask5}개")

# 사용자의 나이를 입력 받아 버스 요금을 계산하는 프로그램을 작성하시오.
# 버스 기본 요금 : 1500원
# - 5살 미만 영유아는 기본 요금의 50% 할인
# - 5살 이상 20살 미만 어린이, 청소년들에게는 기본 요금의 25%를 할인
# - 65세 이상 노인에게는 기본 요금의 75%를 할인
age = int(input("나이 입력 >> "))
fee = 1500

if age >= 65 :
    fee *= 0.25
elif age < 20 :
    fee *= 0.75
elif age < 5 :
    fee *= 0.5

print(f"요금은 {int(fee)}원 입니다.")