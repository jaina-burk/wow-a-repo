class Car():
    def __init__(
            self, make='Unknown', model='Unknown', year=None, num_doors=4, owner=None):
        self.make = make
        self.model = model
        self.year = year
        self.num_doors = num_doors
        self.owner = owner

    def describe_car(self):
        print("This car is a(n) %s %s %s." % (self.year, self.make, self.model))
        print("This car is owned by %s and has %s doors." % (self.owner, self.num_doors))

    def change_owner(self):
        new_owner = input("Who is the new owner, replacing %s: " % self.owner)
        self.owner = new_owner
        print("The new owner of this car is %s. " % self.owner)

car_one = Car(make='Toyota', model='Corolla', year=2016, owner='Jaina')
car_two = Car(make='Lincoln', model='Towncar', year=1999, num_doors=2, owner='Jeff')

car_one.describe_car()
car_two.describe_car()

car_two.change_owner()
car_two.describe_car()