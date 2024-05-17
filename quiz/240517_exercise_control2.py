# 간단한 자판기 프로그램을 작성하시오.
# - 메뉴 출력 : 1. 콜라 (600원), 2. 사이다 (800원), 3. 물 (1,000원)
# - 돈 입력 (600원 이상)
#  - 600원 미만 시, 돈을 더 투입하라는 문구 출력
# - 결과 확인
#  - 1 ~ 3번 메뉴가 아닐 시 ‘잘못된 메뉴’ 출력
#  - 메뉴 선택 후 금액 부족 시, ‘금액 부족’ 출력
#  - 잔돈 출력 (1000원, 500원, 100원  개수로 출력)
print("==========================================")
print("================= 자판기 ==================")
print("==========================================")
print("==[1. 콜라]=[2. 사이다]=[3. 물]==[insert]]==")
print("==========================================")
print("===[600]====[800]====[1000]====[000원]]===")
print("==========================================")
print("==========================================")
print("======                              ======")
print("======                              ======")

# coin = int(input("insert coin!! >> "))
# left = coin
#
# if coin < 600 :
#     print("insert more coin;-(")
# else :
#     menu = int(input("press the menu >> "))
#     if menu == 1 :
#         if coin >= 600 :
#             left = coin - 600
#         else :
#             print("금액 부족")
#     elif menu == 2 :
#         if coin >= 800 :
#             left = coin - 800
#         else :
#             print("금액 부족")
#     elif menu == 3 :
#         if coin >= 1000 :
#             left = coin - 1000
#         else :
#             print("금액 부족")
#     else :
#         print("잘못된 메뉴")
#
# print(f"잔돈 : 1,000원 {int(left//1000)}개, 500원 {int(left%1000/500)}개, 100원 {int(left%1000%500/100)}개")

coin = int(input("insert coin!! >> "))

if coin >= 600 :
    menu = int(input("press the menu >> "))
    if menu == 1 :
        coin -= 600
    elif menu == 2 :
        if coin >= 800 :
            coin -= 800
        else :
            print("금액 부족")
    elif menu == 3 :
        if coin >= 1000 :
            coin -= 1000
        else :
            print("금액 부족")
    else :
        print("잘못된 메뉴")
else :
    print("insert more coin;-(")

print(f"잔돈 : 1,000원 {int(coin//1000)}개, 500원 {int(coin%1000//500)}개, 100원 {int(coin%1000%500//100)}개")