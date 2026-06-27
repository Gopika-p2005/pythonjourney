class Employee:

    def __init__(self,name,id,department):
        
        self.name=name

        self.id= id

        self.department=department

    def display_employee(self):

        print(self.name,self.id,self.department)

class Developer(Employee):

    def __init__(self, name, id, department,prgm_lan,frame_wrk):
        
        super().__init__(name, id, department)

        self.prgm_lang=prgm_lan

        self.frame_wrk=frame_wrk

    def display_developer(self):

        print(self.prgm_lang,self.frame_wrk)

developer_instance=Developer("anju",231,"developer","java","CSS")

developer_instance.display_developer()

developer_instance.display_employee()
