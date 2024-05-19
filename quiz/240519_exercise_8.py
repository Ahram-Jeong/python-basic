# 답을 연속으로 맞출수록 점수가 커지는 O/X 퀴즈가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# 예를 들어, "OOXXOXXOOO"의 점수는 총 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# 10번 문제의 점수는 3이 된다. O/X 퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
# (퀴즈의 개수가 달라져도 계산되어야 한다.)

# 출력 예시
# OX 입력 >>  OOOXXO
# 7점
result = input("OX 입력 >> ")
score = 0
total = 0

for i in result:
    if i == "O":
        score += 1
        total += score
    else:
        score = 0

print(f"{total}점")