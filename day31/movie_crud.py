class Movie:

    def __init__(self):
        
        self.fillms=[]

    def add_movie(self,**kwargs):

        self.fillms.append(kwargs)

        print("movie has been added")

    def list_movie(self):

        print(self.fillms)

    def retrieve_movie(self,id=None):

        data=[m for m in self.fillms if m["id"]==id][0]

        print(data)

    def update_movie(self,id=None,**kwargs):

        movie=[m for m in self.fillms if m["id"]==id][0]

        movie.update(kwargs)

        print("movie has been updated.....................")

    def delete_movie(self,id=None):
        
        movie=[m for m in self.fillms if m["id"]==id][0]

        self.fillms.remove(movie)

        print("movie has been deleted......")

movie_instance=Movie()

movie_instance.add_movie(id=1,title="kgf",gener="action",language="thelugu",run_time=160)

movie_instance.add_movie(id=2,title="kgf2",gener="action",language="thelugu",run_time=160)

movie_instance.add_movie(id=3,title="drishyam",gener="drama",language="malayalam",run_time=120)

#movie_instance.list_movie()

#movie_instance.retrieve_movie(2)

movie_instance.update_movie(id=3,gener="thriller",run_time=140)

movie_instance.delete_movie(id=2)

movie_instance.list_movie()
