# comparison operator
record = "woodz"
match = "woodz"
print(record == match) # True

# logical operators
# and, or
print(1 > 2 and 2 == 2) # False
print(3 > 2 and 2 == 2) # True
print(1 > 2 or 2 == 2) # True

user_input = "mypassword"
stored_password = "mypassword"
print(user_input == stored_password) # True

# Q : 문자열 my_string1과 my_string2가 대문자 "A"로 시작하고, 그리고 소문자 "a"로 끝나는지 그 여부를 출력하는 print문을 작성하세요. True 또는 False의 부울린 값을 출력할 수 있는지 확인하고자 합니다.
my_string1 = "Alpha"
my_string2 = "Anaconda"

print((my_string1[0] and my_string2[0] == "A") and (my_string1[-1] and my_string2[-1] == "a"))