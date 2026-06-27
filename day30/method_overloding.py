class Calculator:

    def add(self,num1,num2):

        return num1+num2
    
    def add(self,num1,num2,num3):

        return num1+num2+num3
    
    def add(self,num1,num2,num3,num4):

        return num1+num2+num3+num4
    
calculator_instance=Calculator()

calculator_instance.add(100,200)
#calculator_instance.add(100,200,300)
calculator_instance.add(100,200,300,400)

