class Vehicle:

    def __init__(self):
        
        self.vehicle_list=[]

    def post(self,**kwargs):

        self.vehicle_list.append(kwargs)

        print("add vehicle successfully...")

    def get(self):

        print(self.vehicle_list)

    def retrive(self,id):

        data=[v for v in self.vehicle_list if v["id"]==id][0]

        print(data)

    def put(self,id=None,**kwargs):

        data=[v for v in self.vehicle_list if v["id"]==id][0]

        data.update(kwargs)

        print("update successfully.....")

    def delete(self,id=None):
        
        veh=[v for v in self.vehicle_list if v["id"]==id][0]

        self.vehicle_list.remove(veh)

        print("delte successfully....")

vehicle_instance=Vehicle()

vehicle_instance.post(id=1,name="toyota innova",owner_type="individual",running_km=45000,condition="good",location="kochi",source="OLX")

vehicle_instance.post(id=2,name="hyundai",owner_type="Dealer",running_km=32500,condition="excellent",location="malappuram",source="CarTrade")

vehicle_instance.post(id=3,name="maruthi swift",owner_type="individual",running_km=68000,condition="good",location="malappuram",source="Facebook")

vehicle_instance.put(id=3,location="calicut",condition="fair")

vehicle_instance.delete(id=2)

vehicle_instance.retrive(id=3)

vehicle_instance.get()