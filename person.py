import random
from school import School
class Person:
    def __init__(self,name) -> None:
        self.name=name

class Teacher ( Person):
    def __init__(self, name) :
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(33,100)
    
class Student(Person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.classroom=classroom
        self._id=None
        self.marks={}
        self.subject_grade={}
        self.grade=None

    def calculate_final_grade(self):
        sum =0
        for grade in self.subject_grade.values():
            point=School.grade_to_value(grade)
            sum+=point
        gpa=sum/len(self.subject_grade)
        self.grade=School.value_to_grade(gpa)

    @property
    def id(self):
        returnself. __id
    @id.setter
    def __id(self,value):
        self.__id=value




    - Methods:
        - calculate_final_grade(): Calculates the final grade of the student.
    - Properties:
        - id: Getter and setter for student ID.
