from math import sqrt
from time import sleep

class Rocket():
    def __init__(self, x=0, y=0, weight=100, capacity=4, speed=400, name=None):
        self.x = x
        self.y = y
        # Weight in lbs
        self.weight = weight
        # Number of crew
        self.capacity = capacity
        # Speed in kms
        self.speed = speed
        # Sets name if provided
        self.name = name

    def move_rocket(self, x_increment=0, y_increment=0):
        self.x += x_increment
        self.y += y_increment

    def get_distance(self, other_rocket):
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
    def launch(self):
        if self.name != None:
            print("The rocket %s has launched!" % self.name)
        else:
            print("The unnamed rocket has launched!")

    def land_rocket(self):
        print("The rocket has started the descent at %s, %s" % (self.x, self.y))
        sleep(1)
        self.y = 0
        print("The rocket has safely landed at %s, %s" % (self.x, self.y))

class Shuttle(Rocket):
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x,y)
        self.flights_completed = flights_completed