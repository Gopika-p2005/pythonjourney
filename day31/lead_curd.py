class Lead:

    def __init__(self):

        self.lead_list=[]

    def post(self,**kwargs):

        self.lead_list.append(kwargs)

        print("add successfully....")

    def get(self):

        print(self.lead_list)

    def retrive(self,id=None):

        data=[l for l in self.lead_list if l["id"]==id][0]

        print(data)

    def put(self,id=None,**kwargs):

        data=[l for l in self.lead_list if l["id"]==id][0]

        data.update(kwargs)

        print("update successfully....")

    def delete(self,id=None):

        data=[l for l in self.lead_list if l["id"]==id][0]

        self.lead_list.remove(data)

        print("delete successfully....")

lead_instance=Lead()

lead_instance.post(id=1,name="anjali",contact="anjali@gmail.com",status="interested",course="python full stack",source="wedsite")

lead_instance.post(id=2,name="rahul",contact="rahul@gmail.com",status="follow_up",course="data science",source="instagram")

lead_instance.post(id=3,name="meera",contact="anjali@gmail.com",status="interested",course="machine learning",source="wedsite")

lead_instance.put(id=3,contact="meera@gmail.com",status="enrolled",source="referral")

lead_instance.retrive(id=3)

lead_instance.delete(id=1)

lead_instance.get()