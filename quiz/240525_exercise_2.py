# Q. 치킨집에서 치킨 요리 시간을 줄이고자 대기 손님을 대상으로 치킨 자동 주문 시스템을 개발하였다.
# 시스템 코드를 확인하고 적절한 예외 처리를 하시오.

# 조건 1 : 1보다 작거나 숫자가 아닌 입력 값이 들어올 때는 ValueError로 처리하고 "잘못된 값을 입력하였습니다." 출력
# 조건 2 : 주문 가능한 총 치킨은 10마리 이며 모두 소진 시, 사용자 정의 에러 SoldOutError를 발생시키고 프로그램 종료, "재고 소진으로 인한 주문 불가" 출력

chicken = 10
waiting = 1

class SoldOutError(Exception) :
    pass

while (True):
    try :
        print(f"남은 치킨 : {chicken} 마리")
        order = int(input("주문 할 치킨 수량 >> "))
        
        if order <= 0 or type(order) != int : # type(order) != int 를 빼도 정상 동작
            raise ValueError
        elif order > chicken :
            print("재료가 부족합니다.")
            raise SoldOutError("재고 소진으로 인한 주문 불가")
        else :
            print(f"대기 번호 {waiting} 번 : {order}마리 주문 완료")
            waiting += 1
            chicken -= order

        if chicken == 0 :
            raise SoldOutError
    except ValueError :
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as e :
        print(e)
        break