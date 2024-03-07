class Person():
    def __init__(self, name='Unknown', age=None, birthplace=None):
        self.name = name
        self.age = age
        self.birthplace = birthplace

    def introduce_yourself(self):
        if self.birthplace != None:
            print("Hello, my name is %s and I'm from %s." % (self.name, self.birthplace))
        else:
            print("Hello, my name is %s." % self.name)

    def age_person(self, age_increment=1):
        self.age = self.age + age_increment
        print('%s is now %s years old. Woah!' % (self.name, self.age))

class Student(Person):
    def __init__(
            self, name='Unknown', age=None, birthplace=None, gpa=None, graduation_year=2000):
        super().__init__(name,age,birthplace)
        self.gpa = gpa
        self.graduation_year = graduation_year


person_one = Person('Jeff', 20, 'Ohio')
person_two = Person('Jaina', age=32, birthplace='Fairfax, VA')
person_three = Person('Christina')
student_one = Student('Evee', 26, 'Oregon', 4.0, 2020)

student_one.introduce_yourself()
print('My GPA is %s and I graduated in the year %s.' % (student_one.gpa, student_one.graduation_year))

