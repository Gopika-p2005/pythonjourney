class Parent:

    def __init__(self,id,name,salary):

        self.name=name

        self.id=id

        self.salary=salary

class Manager(Parent):

    def __init__(self, id, name, salary,department):

        super().__init__(id, name, salary)

        self.department=department

    def display_manager(self):

        print(self.id,self.name,self.salary,self.department)

    def annual(self):

        annual_salary=self.salary*12

        print("annual salary",annual_salary)

manager_instance=Manager(101,"arun",50000,"HR")

manager_instance.display_manager()

manager_instance.annual()