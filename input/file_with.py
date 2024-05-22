import pickle
# with의 파일 접근 방식
# 1. 파일에 접근
# 2. 파일의 내용 읽기, 쓰기, 수정, 삭제 등을 수행
# 3. 파일 자원 해제 (close)
# with 구문은 파일을 실행했을 때 오류가 발생하든 안하든 마지막에 close 를 반드시 수행
with open("profile.pickle", "rb") as profile_file :
    print(pickle.load(profile_file))

with open("drowning.txt", mode = "w", encoding = "utf-8") as woodz_file :
    woodz_file.write("Oh, I'm drowning\nIt's raining all day")

with open("drowning.txt", mode = "r", encoding = "utf-8") as woodz_file :
    print(woodz_file.read())