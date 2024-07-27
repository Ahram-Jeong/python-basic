sales = ["🍕", "🍔", "🍟", "🌭", "☕"]
for item in sales :
    print(f"Example sale of : {item}")

employees = {"chef" : "Ashley", "ceo" : "WOODZ"}
for position in employees :
    print(f"The {position} is held by {employees[position]}.")
    # The chef is held by Ashley.
    # The ceo is held by WOODZ.

mylist = [("a", "b"), ("c", "d"), (1, 2)]
for item1, item2 in mylist :
    print(f"item1 : {item1}, item2 : {item2}")
    # item1 : a, item2 : b
    # item1 : c, item2 : d
    # item1 : 1, item2 : 2

# Q : my_list1을 반복하는 for 루프를 작성하고, 루프 안에서 매번 값에 42를 추가하여, 그 새로운 결과를 my_list2에 추가하세요. 아무것도 출력하지 않다도 됩니다. mylist2 해답에 대해 여러분의 my_list2답을 확인하고자 합니다.
my_list1 = [1, 2, 3, 4, 5, 10]
my_list2 = []

for i in my_list1:
    my_list2.append(i + 42)

print(my_list2) # [43, 44, 45, 46, 47, 52]