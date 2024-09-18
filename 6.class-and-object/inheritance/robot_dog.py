from robot import Robot

class Robot_Dog(Robot):
    def make_noise(self):
        print('Woof Woof!')
    
    def eat(self):
        super().eat()
        print('I Like bacon!')
