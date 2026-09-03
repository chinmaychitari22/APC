class Exam:
    def __init__(self, marks):
        self.marks = marks

    def display_result(self):
        print("\nExam Information")

        for i, mark in enumerate(self.marks, 1):
            print("Semester", i, "Marks:", mark)

        average = sum(self.marks) / len(self.marks)

        print("Cumulative Average:", round(average, 2))

        if average >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")