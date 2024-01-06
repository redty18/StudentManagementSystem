class Student:
    def __init__(self, id, name, age, grades):
        self.id = id
        self.name = name
        self.age = age
        self.grades = grades
    
    def __str__(self):
        return f"Student Name: {self.name}, Student ID: {self.id}"
    
    def add_student(self, newStudent, studentList):
        if newStudent in studentList:
            print("Not a Unique Student")
        else:
            studentList.append(newStudent)
    
    def display_student_details(self):
        print("Student ID is: ", self.id)
        print("Student Name is: ", self.name)
        print("Student Age is: ", self.age)
        print("Grades: ", end=" ")
        for subject, grades in self.grades.items():
            print(str(subject) + ": " + str(grades))
    
    def find_student_by_id(self, studentList, studentID):
        for student in studentList:
            if student.id == studentID:
                return student
        return None
    
    def calculate_class_average(self, studentList):
        overallGrade = 0
        totalSubject = 0

        for student in studentList:
            overallGrade += sum(student.grades.values())
            totalSubject += len(student.grades)

        average = overallGrade / totalSubject
        return average

student1 = Student(id=1, name="Alice", age=20, grades={"Math": 90, "English": 85, "History": 75})
student2 = Student(id=2, name="Bob", age=21, grades={"Math": 80, "English": 92, "History": 88})
student3 = Student(id=3, name="Charlie", age=22, grades={"Math": 95, "English": 78, "History": 89})

new_student = Student(id=4, name="Mayank", age=20, grades={"Math": 10, "English": 25, "History": 58})

studentList = []
student1.add_student(student1, studentList)
student2.add_student(student2, studentList)
student3.add_student(student3, studentList)
new_student.add_student(new_student, studentList)

print(student1.find_student_by_id(studentList, 3))
print(student1.calculate_class_average(studentList))

