# Q. 당신은 Cocoa 서비스를 이용하는 택시 기사이다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건 1 : 승객 별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해진다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 한다.

# 출력 예제
# [O] 1번 째 손님 (소요시간 : 15분)
# [ ] 2번 째 손님 (소요시간 : 15분)
# [O] 3번 째 손님 (소요시간 : 15분)
# ...
# [ ] 50번 째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2 명

from random import *

total = 0

for i in range(1, 51) :
    # ridingTime = random.randint(5, 51)
    ridingTime = randrange(5, 51)
    if 5 <= ridingTime <= 15 :
        total += 1
        check = "O"
    else :
        check = " "
    print(f"[{check}] {i}번 째 손님 (소요시간 : {ridingTime}분)")

print(f"총 탑승 승객 : {total} 명")