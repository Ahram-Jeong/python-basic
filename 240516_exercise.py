# Q. 댓글 이벤트를 진행하여 작성자들 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하세요.

# 조건1 : 댓글은 총 20명이 작성하였고, 아이디는 1 ~ 20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되, 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# 🌱 출력 예시
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# 🌱 활용 예제
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))


from random import *
users = range(1, 21) # 1 ~ 20까지 난수 생성
# print(type(users))
users = list(users) # 리스트로 변환
# print(type(users))

# print(users)
shuffle(users) # 섞기
print(users)

winners = sample(users, 4) # 4명 추출. 당첨자 총 4명 중 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print("-- 축하합니다 --")