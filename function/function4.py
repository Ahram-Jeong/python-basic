gun = 10

def checkpoint(soldiers) : # 경계근무
    global gun # 전역 스코프에 있는 gun 사용
    # gun = 20
    gun = gun - soldiers
    print(f"[function 내] 남은 총 : {gun}") # 8

def checkpoint_ret(gun, soldiers) : # 경계근무
    gun = gun - soldiers # 지역 변수
    print(f"[function 내] 남은 총 : {gun}") # 8
    return gun

print(f"전체 총 : {gun}") # 10
# checkpoint(2) # 2명이 경계 근무
gun = checkpoint_ret(gun, 2) # 함수 checkpoint_ret의 반환 값을 전역 변수 gun에 저장
print(f"전체 총 : {gun}") # 8