absent = [2, 5] # 결석
noBook = [7] # 책을 안가져온 학생

for student in range(1, 11) : # 1 ~ 10까지
    if student in absent :
        continue # 아래 코드가 아닌, 다음 반복문을 실행
    elif student in noBook :
        print(f"오늘 수업은 여기까지. {student}번은 교무실로 따라와!")
        break # 반복문을 완전히 빠져 나옴
    print(f"{student}번 나와서 문제 풀어봐.")