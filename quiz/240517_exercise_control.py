import random

# string 배열 생성
weather = ["sunny", "rain", "snow", "fine dust", "wow"]
random.shuffle(weather) # string 배열 셔플
today = random.choice(weather) # 요소 1개 추출

if today == "rain" or today == "snow" :
    print(f"오늘 날씨는 {today} 우산을 챙기세요!")
elif today == "sunny" :
    print(f"오늘 날씨는 {today} 선글라스를 챙기세요!")
elif today == "fine dust" :
    print(f"오늘 날씨는 {today} 마스크를 챙기세요!")
else :
    print("외출하기 좋은 날씨입니다.")
