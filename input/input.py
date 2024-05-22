print("Python", "Java") # Python Java
print("Python" +  "Java") # PythonJava

print("Python", "Java", sep = ",") # Python,Java
print("Python", "Java", "JavaScript", sep = " vs ") # Python vs Java vs JavaScript

print("Python", "Java", sep = ", ", end = "? ") # Python, Java? 무엇이 더 재미있나요?
print("무엇이 더 재미있나요?")

# import sys
# 보통 로그를 남길 때 stdout은 일반적인 내용, stderr은 에러 발생 시 관련 내용을 출력하기 위함
# print("Python", "Java", file = sys.stdout) # 표준 출력
# print("Python", "Java", file = sys.stderr) # 표준 에러

# 시험 성적
scores = {"Java" : 99, "Python" : 50, "JavaScript" : 35}
for sub, score in scores.items() :
    # print(sub, score)
    print(sub.ljust(10), str(score).rjust(4), sep = ":") # ljust() : 왼쪽 정렬, rjust() : 오른쪽 정렬

# 은행 대기 순번표
# 001, 002, 003 ...
for num in range(1, 21) :
    print("대기번호 : " + str(num).zfill(3))

# input으로 받은 값은 항상 str임
answer = input("Write anything : ")
print(f"입력하신 값은 {answer} 입니다.")