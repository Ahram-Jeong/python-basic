# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여 준다.
import pickle

profile_file = open("profile.pickle", "wb") # 바이너리 쓰기
profile = {"name" : "조승연", "age" : 27, "skill" : ["자바", "파이썬", "코틀린"]}
print(profile)
pickle.dump(profile, profile_file) # profile의 내용을 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") # 바이너리 읽기
profile = pickle.load(profile_file) # file의 내용을 profile에 불러오기
print(profile)
profile_file.close()