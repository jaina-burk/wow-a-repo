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

    
    

    
rocket_1 = Rocket(5, 5, 500, 6, 1000, name='Rocket 1')
rocket_2 = Rocket(weight=500, speed=500, name='Rocket 2')
rocket_3 = Rocket(8,9, speed=200, capacity=1, name='Rocket 3')

my_rockets = [rocket_1, rocket_2, rocket_3]

#for rocket in my_rockets:
    #print("Here are this rockets specs for %s: " % rocket.name)
    #print("Position: %s, %s" % (rocket.x, rocket.y))
    #print("Weight in lbs: %s" % rocket.weight)
    #print("Crew capacity: %s " % rocket.capacity)
    #print("Speed (kms): %s \n" % rocket.speed)

rocket_1.launch()
rocket_3.land_rocket()