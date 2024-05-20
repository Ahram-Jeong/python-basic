# Q. 표준 체중을 구하는 프로그램을 작성하시오.
# * 표준 체중 : 각 개인의 키에 적당한 체중
# * 성별에 따른 공식
# 여 : 키(m) * 키(m) * 21
# 남 : 키(m) * 키(m) * 22

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#     - 함수 명 : std_weight
#     - 전달 값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘 째 자리까지 표시

# 출력 예시
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender) : # 키 : m 단위
    if gender == "여자" :
        return height * height * 21
    else :
        return height * height * 22

height = 175 # cm 단위
gender = "남자"
result = round(std_weight(height/100, gender), 2)
print(f"키 {height}cm {gender}의 표준 체중은 {result}kg 입니다.")