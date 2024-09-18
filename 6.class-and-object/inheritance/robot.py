class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print("My robot's name is", name)

    def walk(self, x):
        self.position[0] += x
        print('New Position:', self.position)

    def eat(self):
        print("I'm hungry!")