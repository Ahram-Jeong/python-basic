try :
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 정수 입력 >> ")))
    nums.append(int(input("두 번째 정수 입력 >> ")))
    nums.append(int(nums[0] / nums[1]))
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
except ValueError :
    print("ValueError!")
except ZeroDivisionError as e :
    print(e)
except Exception as e:
    print("Error:(")
    print(e)