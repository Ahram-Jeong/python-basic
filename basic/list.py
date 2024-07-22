myvar = "WOODZ"
mylist = [100, 200, 300, 400, 500]
mylist.append(myvar) # 리스트의 끝에 추가
mylist.insert(0, myvar)# 특정 인덱스의 위치에 추가

print(mylist) # ['WOODZ', 100, 200, 300, 400, 500, 'WOODZ']

item_rm = mylist.pop() # 리스트의 맨 마지막 아이템 제거
print(mylist) # ['WOODZ', 100, 200, 300, 400, 500]
print(item_rm) # WOODZ

mylist.pop(0) # 인덱스 0의 아이템 제거
print(mylist) # [100, 200, 300, 400, 500]

mylist.reverse() # 리스트를 역순으로 출력
print(mylist) # [500, 400, 300, 200, 100]

mylist2 = [4, 7, 3, 98, 34, 23, 76, 44, 88, 11, 34]
mylist2.sort() # 리스트를 오름차순 정렬
mylist2.reverse() # 역순 정렬
print(mylist2) # [98, 88, 76, 44, 34, 34, 23, 11, 7, 4, 3]