class Agent():
    origin = "USA"

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

x = Agent("WOODZ", 181, 170)
print(x.weight) # 170
x.weight = 70
print(x.weight) # 70