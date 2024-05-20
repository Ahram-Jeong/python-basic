# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print(f"이름 : {name},\t나이 : {age}세\t", end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language) :
    print(f"이름 : {name},\t나이 : {age}세\t", end = " ")
    for i in language :
        print(i, end = " ")
    print()

profile("조승연", 28, "Python", "Java", "Kotlin", "C#", "Javascript", "C")
profile("황민현", 25, "Java", "Swift")
