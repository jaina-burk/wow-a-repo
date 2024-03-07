from math import sqrt

class Rocket():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=0):
        self.x += x_increment
        self.y += y_increment

    def get_distance(self, other_rocket):
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance

my_rockets = [Rocket() for x in range(0,3)]

my_rockets[0].move_rocket(5,-4)
my_rockets[1].move_rocket(-3,0)
my_rockets[2].move_rocket(1000,-1000)

for rocket in my_rockets:
    print("This rocket is at %s, %s." % (rocket.x, rocket.y))

print("The rocket 0 and 1 are %f units apart." % my_rockets[0].get_distance(my_rockets[1]))
print("The rocket 1 and 2 are %f units apart." % my_rockets[1].get_distance(my_rockets[2]))