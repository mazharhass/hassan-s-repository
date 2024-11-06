class Person:
  def __init__(self, name: str, address: str):
    self.name = name
    self.address = address
    
  def get_name(self):
    return self.name
    
  def get_address(self):
    return self.address
    
  def set_name(name: str):
    self.name = name
    
  def set_address(address: str):
    self.address = address
    
class Student(Person):
  def __init__(self, name, address, student_id: int, grade: int)
    super().__init__(name, address) 
  def get_student_id():
    return self.student_id
  def get_grade():
    return self.grade
  def set_student_id(student_id: int):
    self.student_id = student_id
  def set_grade(grade: int):
    self.grade = grade

class Teacher(Person):
