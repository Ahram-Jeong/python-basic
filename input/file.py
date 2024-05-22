music_file = open("music.txt", mode = "w", encoding = "utf-8") # w : 쓰기 모드
print("WOODZ : Drowning", file = music_file)
print("황민현 : Hidden side", file = music_file)
music_file.close()

##########################################################################################################

music_file = open("music.txt", mode = "a", encoding = "utf-8") # a : 추가 모드 (append)
music_file.write("뉴진스 : Hype boy")
music_file.write("\nDAY6 : 한 페이지가 될 수 있게")
music_file.close()

##########################################################################################################

music_file = open("music.txt", mode = "r", encoding = "utf-8") # r : 읽기 모드
print(music_file.read())
music_file.close()

##########################################################################################################

music_file = open("music.txt", mode = "r", encoding = "utf-8") # r : 읽기 모드
print(music_file.readline(), end = "") # 읽기 모드로 연 후 readline()을 사용하여 파일을 줄 별로 읽기
print(music_file.readline(), end = "")
print(music_file.readline(), end = "")
print(music_file.readline(), end = "")
music_file.close()

##########################################################################################################

music_file = open("music.txt", mode = "r", encoding = "utf-8") # r : 읽기 모드
while True :
    line = music_file.readline()
    if not line :
        break
    print(line, end = "")
music_file.close()

##########################################################################################################

music_file = open("music.txt", mode = "r", encoding = "utf-8") # r : 읽기 모드
lines = music_file.readlines() # list 형태로 저장
print(type(lines)) # <class 'list'>

for line in lines :
    print(line, end="")
music_file.close()