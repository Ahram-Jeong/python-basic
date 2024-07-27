n = 1

while n < 5 :
    print(f"N is currently : {n}")
    n += 1

# Q : 0에서 1000(1000 포함)의 값을 가지는 my_list라는 리스틀 만드는 루틴을 구현하세요.
my_list = []
n = 0

while n <= 1000 :
    my_list.append(n)
    n += 1

print(my_list)