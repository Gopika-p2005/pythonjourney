class User:

    def __init__(self,username,email):

        self.username=username

        self.email=email

class Child(User):

    def __init__(self, username, email,course,progress_percentage):

        super().__init__(username, email)

        self.course=course

        self.progress_percentage=progress_percentage

    def display_child(self):

        print(self.username,self.email,self.course,self.progress_percentage,"%")

        if self.progress_percentage==100:

            print("course completed")

        else:

            print("course not completed")

Child_instance=Child("arun","arun1@gmail.com","python",100)

Child_instance.display_child()
