#Add ID 101: “Alice”, Grade: “A” 
# Update ID 101: Grade: “A+” 
# Expected Output: ID: 101 | Name: Alice | Grade: A+

class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def update_grade(self, new_grade):
        self.grade = new_grade

    def display_info(self):
        return f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade}"
    
object = Student(101, "Alice", "A") 
object.update_grade("A+")
print(object.display_info())    