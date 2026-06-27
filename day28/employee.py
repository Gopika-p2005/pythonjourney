class employee:

    def set_attrs(self,name,desig,sal,gender):

        self.name=name

        self.desig=desig

        self.sal=sal

        self.gender=gender

    def display_attrs(self):

        print(self.name,self.desig,self.sal,self.gender)

emp1=employee()

emp1.set_attrs("rohan","qa",56000,"male")

emp1.display_attrs()