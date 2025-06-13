# University Management System
# Current studies - > Class vars, inheritance, multiple inheritance, super()
# abstract classes, polymorphism, encapsulation, magic methods

from abc import ABC, abstractmethod
class University: 
    def __init__(self, id, course) -> None:
        # instance variables
        self.id = id
        self.course = course

class Cacl2_class(University):
    @abstractmethod
    def get_class(self):
        pass

class Staff(University):
    # Class variables
    number_staffs = 0

    def __init__(self, id, course) -> None:
        super().__init__(id, course)
        Staff.number_staffs += 1

class Student(University):

    number_student = 0
    def __init__(self, id, course) -> None:
        super().__init__(id, course)
        Student.number_student += 1


lecturer = Staff('123123', 'Science')
print(lecturer.id)

student1 = Student('175050', 'Comp Sci')
print(student1.course)

