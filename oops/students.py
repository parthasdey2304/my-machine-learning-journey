class student:
    def __init__(self, name, stream, marks):
        self.name = name
        self.stream = stream
        self.marks = marks

    def get_student_data(self):
        print(f"The student {self.name} from {self.stream} has scored {self.marks}")
