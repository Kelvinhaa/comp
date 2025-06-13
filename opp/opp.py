# University Management System
# Current studies - > Class vars, inheritance, multiple inheritance, super()
# abstract classes, polymorphism, encapsulation, magic methods

from abc import ABC, abstractmethod
class University: 
    def __init__(self, id, course) -> None:
        # instance variables
        self.id = id
        self.course = course

    # Magic methods
    # This method is called when the object is printed
    def __str__(self) -> str:
        return f''
    # This method is called when the object is represented
    def __repr__(self) -> str:
        pass

class Calc2_class(University):
    @abstractmethod
    def get_class(self):
        pass

class Staff(University):
    # Class variables
    number_staffs = 0
    
    def __init__(self, id, course) -> None:
        super().__init__(id, course)
        Staff.number_staffs += 1

    def get_class(self):
        return f'Staff ID: {self.id}, Course: {self.course}'

class Student(University):

    number_student = 0
    def __init__(self, id, course) -> None:
        super().__init__(id, course)
        Student.number_student += 1

    def get_class(self):
        return f'Student ID: {self.id}, Course: {self.course}'


# Example usage
# Creating instances of Staff and Student
# and calling their methods
lecturer = Staff('123123', 'Science')
print(lecturer.get_class())

student1 = Student('175050', 'Comp Sci')
print(student1.course)

