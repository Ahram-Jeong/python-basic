# if 조건 :
#     실행 코드
# elif 조건 :
#     실행 코드
# else :
#     실행 코드

# Ex1
weather = input("Today's weather (sunny, rain, snowy, fine dust..) >> ")
if weather == "rain" or weather == "snowy":
    print("You need an umbrella!")
elif weather == "sunny" :
    print("You need sunglasses!")
elif weather == "fine dust" :
    print("You need a mask!")
else :
    print("You don't need anything!")

# Ex2
temp = int(input("오늘의 기온 >> "))
if 30 <= temp :
    print("너무 더우니 외출을 삼가하세요.")
elif 10 <= temp < 30 :
    print("좋은 날씨입니다.")
elif 0 <= temp < 10 :
    print("겉옷을 챙기세요.")
else :
    print("매우 추운 날씨입니다.")