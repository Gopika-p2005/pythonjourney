class Person:

    def __init__(self,name,age):

        self.name=name

        self.age=age

class Teacher(Person):

    def __init__(self, name, age,sub,monthly_salary):

        super().__init__(name, age)

        self.subject=sub

        self.monthly_salary=monthly_salary


    def display_teacher(self):

        print(self.name,self.age,self.subject,self.monthly_salary)

    def annual(self):

        total=self.monthly_salary*12

        print("annual salary",total)

Teacher_instance=Teacher("meera",35,"maths",40000)

Teacher_instance.display_teacher()

Teacher_instance.annual()