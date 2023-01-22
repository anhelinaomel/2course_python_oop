# The class GROUP contains a sequence of instances of the class STUDENT. The class STUDENT contains the student's name,
# surname, record book number and grades. Determine the required attributes-data and attributes-methods in classes GROUP
# and STUDENT. Find the average score of each student. Output to the standard output stream the five students with the 
# highest average score. Assume that there can be no more than 20 students in a group, as well as students with the same name and surname.
# No more than 20 students in a group, as well as students with the same name and surname

class Student:
    def __init__(self, name = "", surname = "", record_num = 0):
        self.name = name
        self.surname = surname
        self.record_num = record_num
        self.grades = dict()

    def set_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_avg_grade(self):
        grade_sum = 0
        for item in self.grades.values():
            grade_sum = grade_sum + item
        return grade_sum / len(self.grades)

class Group:
    def __init__(self, gname = "", student = list()):
        self.gname = gname
        self.students = student

    def add_student(self, student):
        i = 0
        inserted = 0
        student_avg_grade = student.get_avg_grade()
        for item in self.students:
            if item.get_avg_grade() <= student_avg_grade:
                self.students.insert(i, student)
                inserted = 1
                break
            i = i + 1
        if not inserted:
            self.students.append(student)

    def get_top_students(self):
        i = 0
        for item in self.students:
            if i == 5:
                break
            print(item.name, item.surname, item.record_num, item.get_avg_grade())
            i = i + 1

student0 = Student("Shadab", "Alam", 234788)
student0.set_grade("math", 5)
student0.set_grade("history", 5)
student0.set_grade("sports", 5)
student0.set_grade("english", 5)

student1 = Student("Shadab", "Bachchan", 234789)
student1.set_grade("math", 6)
student1.set_grade("history", 6)
student1.set_grade("sports", 6)
student1.set_grade("english", 6)

student2 = Student("Figo", "Beauty", 234791)
student2.set_grade("math", 1)
student2.set_grade("history", 4)
student2.set_grade("sports", 6)
student2.set_grade("english", 11)

student3 = Student("Ivo", "Bobul", 234790)
student3.set_grade("math", 9)
student3.set_grade("history", 9)
student3.set_grade("sports", 9)
student3.set_grade("english", 9)

student4 = Student("Coco", "Jumbo", 234792)
student4.set_grade("math", 7)
student4.set_grade("history", 8)
student4.set_grade("sports", 2)
student4.set_grade("english", 5)

student5 = Student("Beta", "Alpha", 234793)
student5.set_grade("math", 10)
student5.set_grade("history", 11)
student5.set_grade("sports", 10)
student5.set_grade("english", 10)

group123 = Group(gname = "TVz-11")

group123.add_student(student0)
group123.add_student(student1)
group123.add_student(student2)
group123.add_student(student3)
group123.add_student(student4)
group123.add_student(student5)

group123.get_top_students()