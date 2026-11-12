class Student:
    def __init__(self, name, age, birth_year, fav_color):
        self.name = name 
        self.age = age
        self.birth_year = birth_year
        self.fav_color = fav_color

    def display(self):
        print(self.name, self.age, self.birth_year, self.fav_color)

student1 = Student("Ryan", 13, 2013, "Blue")
#student1.display()

class Marks(Student):
    def __init__(self, maths, english, chemistry, biology, physics, name, age, birth_year, fav_color):
        super().__init__(name, age, birth_year, fav_color)
        self.maths = maths
        self.english = english
        self.chemistry = chemistry
        self.biology = biology
        self.physics = physics

    def display2(self):
        print(self.name, self.maths, self.english, self.chemistry, self.biology, self.physics)

student1marks = Marks(85, 91, 75, 69, 98, "Ryan", 13, 2013, "Blue")
student1marks.display2()
