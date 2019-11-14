# Create a student class with class variable college_name, college_address and instance varible student_name, student_id.
# Display all student details with Student class object

class student:
    _registry = []
    college_name = 'GPCET'
    college_address = 'kurnool'

    def __init__(self, student_name, student_id):
        self._registry.append(self)
        self.student_name = student_name
        self.student_id = student_id

    def display_student_details(self):
        print('#############################')
        print('Name: ', self.student_name)
        print('Id: ', self.student_id)
        print('college name: ', student.college_name)
        print('college address: ', student.college_address)


std1 = student('chandrakala', 1)
std2 = student('sowmya', 2)
std3 = student('Amrutha', 3)
std4 = student('Prathima', 4)

for p in student._registry:
    p.display_student_details()