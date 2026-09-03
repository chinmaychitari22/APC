class Student:
    def __init__(self, name, student_class, mobile):
        self.name = name
        self.student_class = student_class
        self.mobile = mobile

    def display_info(self):
        print("Student Information")
        print("Name:", self.name)
        print("Class:", self.student_class)
        print("Mobile Number:", self.mobile)