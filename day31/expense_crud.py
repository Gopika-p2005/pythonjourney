class Expense:

    def __init__(self):
    
        self.expense_list=[]

    def post(self,**kwargs):

        self.expense_list.append(kwargs)

        print("adding successfully......")

    def get(self):

        print(self.expense_list)

    def retrive(self,id=None):

        data=[e for e in self.expense_list if e["id"]==id][0]

        print(data)

    def put(self,id=None,**kwargs):

        data=[e for e in self.expense_list if e["id"]==id][0]

        data.update(kwargs)

        print("update successfully....")

    def delete(self,id=None):

        data=[e for e in self.expense_list if e["id"]==id][0]

        self.expense_list.remove(data)

        print("delete suucessfully.....")

expense_instance=Expense()

expense_instance.post(id=1,name="groceries",category="food",amount=2500,date=15/6/2026,method="UPI")

expense_instance.post(id=2,name="petrol",category="transport",amount=1000,date=18/6/2026,method="cash")

expense_instance.post(id=3,name="groceries",category="food",amount=1500,date=15/6/2026,method="UPI")

expense_instance.put(id=3,name="eletricity bill",category="utillities",date=20/6/2026,method="net banking")

expense_instance.retrive(id=3)

expense_instance.delete(id=2)

expense_instance.get()