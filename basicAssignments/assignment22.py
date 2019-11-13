# Create student class with instance, class and static methods.

class Student:

    school = 'GGK'

    def __init__(self, marks1, marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def average(self):
        print('instance method called', self)
        return (self.marks1 + self.marks2)/2

    @classmethod
    def getSchoolInfo(cls):
        print('class method called', cls)
        return cls.school

    @staticmethod
    def staticmethod():
        print('static method called')

obj = Student(20,30)

print(obj.average())

print(Student.average(obj))  # another way of calling instance method

print(obj.getSchoolInfo())

obj.staticmethod()