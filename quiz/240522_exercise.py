# Q. 회사에서 매주 1회 작성해야 하는 보고서가 있다.
# 보고서는 항상 아래와 같은 형태로 출력해야 한다.

# - n주차 주간 보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1 ~ 50주차 까지의 보고서 파일을 생성하는 프로그램을 작성하시오.
# 조건 : 파일 명은 '1주차.txt', '2주차.txt', '3주차.txt' 와 같이 생성

for i in range(1, 51) :
    with open(str(i) + "주차.txt", mode = "w", encoding = "utf-8") as report_file :
        report_file.write(f"- {i}주차 주간 보고 -\n")
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : ")