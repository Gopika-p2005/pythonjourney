class Sports:

    def __init__(self,name):
        
        self.name=name

class Cricket(Sports):

    def __init__(self,name,players,format):

        super().__init__(name)

        self.players=players

        self.format=format

    def display_cricket(self):

        print(self.name,self.players,self.format)

cricket_instance=Cricket("cricket",11,"sp2")

cricket_instance.display_cricket()