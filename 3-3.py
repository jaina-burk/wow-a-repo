from math import sqrt
from random import randint

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed
        
        
# Create several shuttles and rockets, with random positions.
#  Shuttles have a random number of flights completed.
shuttles = []
for x in range(0,3):
    x = randint(0,100)
    y = randint(1,100)
    flights_completed = randint(0,10)
    shuttles.append(Shuttle(x, y, flights_completed))

rockets = []
for x in range(0,3):
    x = randint(0,100)
    y = randint(1,100)
    rockets.append(Rocket(x, y))
    
# Show the number of flights completed for each shuttle.
for index, shuttle in enumerate(shuttles):
    print("Shuttle %d has completed %d flights." % (index, shuttle.flights_completed))
    
print("\n")    
# Show the distance from the first shuttle to all other shuttles.
first_shuttle = shuttles[0]
for index, shuttle in enumerate(shuttles):
    distance = first_shuttle.get_distance(shuttle)
    print("The first shuttle is %f units away from shuttle %d." % (distance, index))

print("\n")
# Show the distance from the first shuttle to all other rockets.
for index, rocket in enumerate(rockets):
    distance = first_shuttle.get_distance(rocket)
    print("The first shuttle is %f units away from rocket %d." % (distance, index))