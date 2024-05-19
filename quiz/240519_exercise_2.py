# list
lst1 = [2, 5, 7, 8, 10]
print(lst1[0])
print(lst1[3])
print(lst1[2] + lst1[-1]) # 7 + 10

lst2 = [1, 2, 3, ['a', 'b', 'c']]
print(lst2[3][1]) # b
tmp = lst2[3]
print(tmp)
print(tmp[1]) # b

lst4 = [1, 2, 3]
lst5 = [3, 4, 5, 6]
print(lst4 + lst5) # [1, 2, 3, 3, 4, 5, 6]

# 리스트.append()
# 맨 뒤에 값 추가
fruits = ["사과", "포도", ["수박", "메론"], "복숭아", "딸기", "오렌지"]
# ['사과', '오렌지', '수박'] 출력하시오.
cart = []

apple = fruits[0]
waterMelon = fruits[2][0]
orange = fruits[-1]

cart.append(apple)
cart.append(orange)
cart.append(waterMelon)

print(cart) # ['사과', '오렌지', '수박']

# 리스트.insert(인덱스, 값)
# 인덱스 위치에 값 추가
music_list = [
    ["Drowning", "WOODZ"],
    ["Ditto", "뉴진스"],
    ["Supernova", "에스파"]
]
print(music_list) # [['Drowning', 'WOODZ'], ['Ditto', '뉴진스'], ['Supernova', '에스파']]

music_list.insert(1, ["Wish you hell", "웬디"])
music_list.insert(3, ["Bye My Monster", "ONF"])

print(music_list) # [['Drowning', 'WOODZ'], ['Wish you hell', '웬디'], ['Ditto', '뉴진스'], ['Bye My Monster', 'ONF'], ['Supernova', '에스파']]

index_value = int(input("인덱스 입력 >> "))
song = input("노래 입력 >> ")
singer = input("가수 입력 >> ")

music_list.insert(index_value, [song, singer])

print(music_list)

# del 예약어 => del 리스트[i]
# 인덱스 삭제
list7 = [0, 1, 2, 3, 4, 5]
del list7[1]
print(list7) # [0, 2, 3, 4, 5]

list7 = [0, 1, 2, 3, 4, 5]
del list7[1:5]
print(list7) # [0, 5]

# 리스트.remove()
# 값 삭제
list7 = ['a', 'b', 'c', 'd', 'e']
list7.remove('b')
print(list7) # ['a', 'c', 'd', 'e']

# 리스트.sort()
# 리스트에 있는 값을 오름차순 정렬
list8 = [9, 77, 13, 51, 100, 3]
list8.sort()
print(list8) # [3, 9, 13, 51, 77, 100]

# 리스트.reverse()
# 리스트 내의 요소들을 거꾸로 출력
list9 = [9, 77, 13, 51, 100, 3]
list9.reverse()
print(list9) # [3, 100, 51, 13, 77, 9]

# sort() 함수 내 reverse=True로 설정하면 내림차순 정렬
list10 = [9, 77, 13, 51, 100, 3]
list10.sort(reverse=True)
print(list10) # [100, 77, 51, 13, 9, 3]

# 리스트.index()
# 찾고자 하는 값의 위치 출력
list11 = ['a', 'b', 'c', 'd', 'e', 'f']
list11.index('c') # 2

# 리스트.pop()
# 마지막 값을 출력 후 리스트에서 제거
list12 = ['a', 'b', 'c', 'd', 'e', 'f']
list12.pop() # f

# len(리스트)
# 리스트 내부의 값 개수 출력
list13 = [0, 1, 2]
len(list13) # 3

# 튜플 (요소1, 요소2, 요소3..)
# 순서 O, 추가/수정/삭제 불가
tuple1 = (0, 1, 2, 3, ('a', 'b', 'c'), 5)
print(tuple1[2])
print(tuple1[4]) # ('a', 'b', 'c')
print(tuple1[1:3]) # (1, 2)
print(tuple1[3:]) # (3, ('a', 'b', 'c'), 5)

print(len(tuple1)) # 6
# tuple1[0] = 3 # 오류 남

tuple2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(len(tuple2)) # 6

# in : 찾고자 하는 값이 포함되어 있으면 True 반환
# not in : 찾고자 하는 값이 포함되어 있지 않으면 True 반환

str1 = "파이썬 재밌네"
print("파이썬" in str1) # True
print("파이썬" not in str1) # False

list1 = [77, 38, 10]
print(33 in list1) # False
print(33 not in list1) # True

#######################################################
text = "We wish you a merry Christmas!"
search = input("검색할 문자 입력 >> ")

if search in text :
    cnt = text.count(search)
    print(f"{search}은/는 {cnt}번 포함")
else :
    print(f"{search}은/는 없는 문자")