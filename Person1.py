class Person:
      """A base class"""
      def __init__(self, name, age):
          self.name = name
          self.age = age
          

class Student(Person):
      """A derived class for Student"""
      def __init__(self, name, age, school):
        #Person.__init__(self, name, age)
        super().__init__("Student")
        self.name = name
        self.age = age
        self.school = school
      def introduce(self):
        print("hello")



class WorkingAdult(Person):
      """A derived class for WorkingAdult"""
      def __init__(self, name, age, job):
        super().__init__("WorkingAdult")
        self.name = name
        self.age = age
        self.job = job
      def introduce(self):
          print("world")
s1=Student("v1",20,'abd')