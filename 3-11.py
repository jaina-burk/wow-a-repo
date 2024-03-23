from person import *

person_1 = Person("Jaina", age=32, birthplace="Fairfax")
student_1 = Student("Jeff")

print("%s is %s years old and is from %s." %(person_1.name, person_1.age, person_1.birthplace))
print("Student 1 is named %s." % student_1.name)