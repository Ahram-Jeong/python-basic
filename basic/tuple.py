mylist = [1, 2, 3]
mytuple = (1, 2, 3)

print(mytuple)

mylist[0] = "new"
print(mylist) # ['new', 2, 3]

# mytuple[0] = "new"
# print(mytuple) => 변경이 불가하기 때문에 오류 (재할당 불가)

# Q : 값(1, 2, 3, 4, 5)을 가진 my_tuple이라는 튜플을 정의한 다음, my_tuple의 마지막 요소가 10보다 작은지 그 여부를 출력하는 print 문을 작성하세요. 이 print함수의 내부는 부울린 값을 반환하는 간단한 비교 연산자로 작성되어야 합니다. (예 : x <3)
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[-1] < 10)