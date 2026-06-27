class Shape:

    def __init__(self,name):

        self.name=name

class Square(Shape):

    def __init__(self,name,edge):
        
        super().__init__(name)

        self.edge=edge

    def display_square(self):

        print(self.name,self.edge)

Square_instance=Square("square",4)

Square_instance.display_square()