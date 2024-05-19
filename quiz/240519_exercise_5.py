# 6명에 대한 Python 점수가 리스트에 번호 순으로 담겨있다.
# 번호 순서대로 점수와 등급을 출력하시오.
# 80점 이상은 A등급, 60이상 80미만은 B등급, 60미만은 C등급

# 출력 예시
# 1번은 57점 이며, C등급 입니다.
# 2번은 86점 이며, A등급 입니다.
# 3번은 63점 이며, B등급 입니다.
# 4번은 92점 이며, A등급 입니다.
# 5번은 35점 이며, C등급 입니다.
# 6번은 79점 이며, B등급 입니다.

python_score = [57, 86, 63, 92, 35, 79]
num = 1

for score in python_score :
    if score >= 80 :
        grade = "A"
    elif score >= 60 :
        grade = "B"
    else :
        grade = "C"
    print(f"{num}번은 {score}점 이며, {grade}등급 입니다.")
    num += 1