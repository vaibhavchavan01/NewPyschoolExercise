class Person:
    """A base class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        # print(age+age1)
class Student(Person):
    """A derived class for Student"""
    def __init__(self, name, age, school):
        super().__init__(self, name, age, school)

    def introduce(self):
        print('My name is %s. I am %d years old. I am a waiter. I am studying at %s' % self.name, self.age, self.school)

class WorkingAdult(Person):
    """A derived class for WorkingAdult"""
    def __init__(self, name, age, job):
        Person.__init__(self, name, age, job)

    def introduce(self):
        print('My name is %s. I am %d years old. I am studying at %s.' % self.name, self.age, self.job)

person1 = Student("yash", 25, "newSchool")
person2 = WorkingAdult("Yash", 20, "Amazatic")
print(person2)
person1.introduce()
person2.introduce("Yash", 20, "Amazatic")
# person = Person("asd", 20,21)

