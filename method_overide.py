# Practical Task 2

class Adult:
    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def can_drive(self):
        print(f"{self.name} is old enough to drive.")

class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")

# Take user inputs
name = input("Enter name: ")
age = int(input("Enter age: "))
hair_color = input("Enter hair color: ")
eye_color = input("Enter eye color: ")

# Determine the class to instantiate
if age >= 18:
    person = Adult(name, age, eye_color, hair_color)
else:
    person = Child(name, age, eye_color, hair_color)

# Call the can_drive method
person.can_drive()
