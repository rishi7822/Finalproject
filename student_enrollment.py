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


if __name__ == '__main__':
    names = input().split()
    marks = []

    for i in range(len(names)):
        temp = list(map(int, input().split()))
        marks.append(temp)

    cla = list(map(int, input().split()))

    r1 = Result(marks[0][0], marks[0][1], marks[0][2], names[0], cla[0])
    r2 = Result(marks[1][0], marks[1][1], marks[1][2], names[1], cla[1])
    r3 = Result(marks[2][0], marks[2][1], marks[2][2], names[2], cla[2])
    r4 = Result(marks[3][0], marks[3][1], marks[3][2], names[3], cla[3])
    r5 = Result(marks[4][0], marks[4][1], marks[4][2], names[4], cla[4])

    sub = input()
    new_marks = int(input())

    print(r1.calculate_result())
    print(r2.calculate_result())
    print(r3.calculate_result())
    print(r4.calculate_result())
    print(r5.calculate_result())

    print(r1.change_marks(new_marks, sub))
    print(r3.change_marks(new_marks, sub))
    print(r5.change_marks(new_marks, sub))
