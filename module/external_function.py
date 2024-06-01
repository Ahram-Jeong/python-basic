# glob() : 인자로 받은 패턴과 이름이 일치하는 모든 파일과 디렉토리의 리스트를 반환
import glob
import time

print(glob.glob("*.py")) # 현재 디렉토리에 있는 모든 py파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리

folder = "sample"

if os.path.exists(folder) :
    print("이미 존재합니다.")
    remove = input("삭제 하시겠습니까? Y/N >>")
    if remove.upper() == "Y" :
        os.rmdir(folder)
        print("삭제 완료!")
else :
    os.makedirs(folder)
    print(folder, "생성 완료:-)")

print(os.listdir()) # glob()와 유사함

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 시간을 str으로 반환

import datetime
print(f"오늘 날짜 : {datetime.date.today()}")

# timedelta() : 두 날짜의 차이를 계산할 때 사용하는 함수
today = datetime.date.today()
diff = datetime.timedelta(days = 100)
print(f"오늘로부터 100일 후의 날짜 : {today + diff}")