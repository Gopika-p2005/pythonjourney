class Movie:

    def __init__(self,title,runtime,gener,language,director):

        self.title=title

        self.runtime=runtime

        self.gener=gener

        self.language=language

        self.director=director

    def display_movie(self):

        print(self.title,self.runtime,self.gener,self.language,self.director)

movie1=Movie("arm",1.58,"action","tamil","sjn")

movie1.display_movie()