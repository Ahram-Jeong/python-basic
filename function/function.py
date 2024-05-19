def open_account() :
    print("새로운 계좌 생성 완료")

# 입금
def deposit(balance, money) :
    print(f"입금이 완료되었습니다. 잔액은 {balance + money}원 입니다.")
    return balance + money

# 출금
def withraw(balance, money) :
    if balance >= money :
        print(f"출금이 완료되었습니다. 잔액은 {balance - money}원 입니다.")
        return balance - money
    else :
        print(f"출금 실패! 잔액은 {balance}원 입니다.")
        return balance

# 야간 출금
def withraw_night(balance, money) :
    commission = 5000
    return commission, balance - money - commission # 반환 값이 튜플 형식

balance = 0
balance = deposit(balance, 10000000)
# print(balance)
balance = withraw(balance, 3000000)
balance = withraw(balance, 8000000)

commission, balance = withraw_night(balance, 2000000)
print(f"수수료는 {commission}원 이며, 잔액은 {balance}원입니다.")