# Practical Task 1

class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office_location(self):
        print("Head office is located in Cape Town")

class OOPCourse(Course):
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print(f"This course is about {self.description}, and the trainer is {self.trainer}.")

    def show_course_id(self):
        print("The course ID is: #12345")

# Create an object of the subclass and call the methods
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()

