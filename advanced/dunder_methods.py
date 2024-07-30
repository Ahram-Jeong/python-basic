class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ : 사용자 정의 객체를 출력할 때, 출력 되기를 원하는 문자열의 표현을 반환 (항상 문자열을 반환)
    def __str__(self):
        return f"{self.title} written by {self.author}"

    # __len__ : 객체의 길이를 출력할 때, 출력 되기를 원하는 정수를 반환 (항상 정수를 반환)
    def __len__(self):
        return self.pages


mybook = Book("All about Python", "Ash", 300)
print(mybook) # All about Python written by Ash
print(len(mybook)) # 300