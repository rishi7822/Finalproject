class Student:
    def __init__(self, name, sClass):
        self.name = name
        self.sClass = sClass
        self.result = 0.0
        print(f"Added student: {name} to the roll of class: {sClass}")

    def get_name(self):
        return self.name

    def publish(self):
        if self.result >= 33.33:
            return f"{self.name} has been promoted to class: {self.sClass + 1}"
        else:
            return f"{self.name} has been retained in class: {self.sClass}"


class Result(Student):
    def __init__(self, subject1, subject2, subject3, name, sClass):
        super().__init__(name, sClass)
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        print(f"{name} obtained {subject1} marks in subject1")
        print(f"{name} obtained {subject2} marks in subject2")
        print(f"{name} obtained {subject3} marks in subject3")

    def calculate_result(self):
        self.result = (self.subject1 + self.subject2 + self.subject3) / 3
        return self.publish()

    def change_marks(self, new_marks, subject):
        if subject == "subject1":
            self.subject1 = new_marks
        elif subject == "subject2":
            self.subject2 = new_marks
        elif subject == "subject3":
            self.subject3 = new_marks
        line1 = f"{self.name} has ordered a recheck in {subject}"
        new_result = self.calculate_result()
        return f"{line1}\nFollowing is the new result: {new_result}"
