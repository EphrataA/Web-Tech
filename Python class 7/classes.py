# A class is a user-defined bluprint or prototype from which objects are created.

# class Point:
#     def _init_(self, x, y):
#        self.x=X
#        self.y=y

# p = Point(3, 5)
# print(p.x)
# print(p.y)

class student():
    def __init__(self, number_of_student ):
       self.student_list = []
       self.number_of_student = number_of_student


    def add_student(self, student_name ):
       if self.number_of_student > len(self.student_list): 
         self.student_list.append(student_name)
       else:
           print('the class is full')
           return False 

    def student_list(self):
        return self.number_of_student

    def avg_result(*marks):
       return sum(marks)

    def avg_mark(self, avg_mark):
        if avg_mark > 75:
            print("Student can register")
        else:
            return False

section1 = student(3)

section1.add_student("abel")
section1.add_student("robert")
section1.add_student("hanna")
section1.add_student("alex")
print(section1.student_list)