from StudentInfo.student import Student
from StudentInfo.exam import Exam


student = Student("Shravan", "Third Year CSE", "9876543210")

marks = [78, 82, 75, 88, 80, 85]

exam = Exam(marks)

student.display_info()
exam.display_result()