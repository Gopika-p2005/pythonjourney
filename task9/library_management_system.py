class Book:

    def __init__(self,title,author):

        self.title=title

        self.author=author

class IssuedBook(Book):

    def __init__(self, title, author,issued_day):

        super().__init__(title, author)

        self.issued_days=issued_day
    
    def display_issuedbook(self):

        print(self.title,self.author,self.issued_days)
    
    def fine(self):

        if self.issued_days>14:

            fine=(self.issued_days-14)*5
        
        else:

            fine=0

        print("fine amount",fine)

IssuedBook_instance=IssuedBook("python basics","abc",20)

IssuedBook_instance.display_issuedbook()

IssuedBook_instance.fine()
