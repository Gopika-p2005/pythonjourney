"""
CRUD (create retrive update delete)
add = > post => create
list=>get
detail(single)=>retrive
update=>put
remove=>delete
"""

class CaloreTracker:

    def __init__(self):

        self.foodlog=[]

    def post(self,**log):

        self.foodlog.append(log)

        print("food log added successfully...")

    def get(self):

        print(self.foodlog)

    def retrive(self,id):

        data=[f for f in self.foodlog if f["id"]==id][0]

        print(data)

    def put(self,id=None,**kwargs):

        food=[f for f in self.foodlog if f["id"]==id][0]

        food.update(kwargs)

        print("food log updated....")

    def delete(self,id=None):

        food=[f for f in self.foodlog if f["id"]==id][0]

        self.foodlog.remove(food)

        print("food is deleted...")


food_instance=CaloreTracker()

food_instance.post(id=1,title="puttu",meal_type="breakfast",calorie=120)

food_instance.post(id=2,title="dosa",meal_type="breakfast",calorie=80)

food_instance.post(id=3,title="meal",meal_type="lunch",calorie=110)

food_instance.post(id=4,title="biriyani",meal_type="dinner",calorie=220)

food_instance.retrive(4)

food_instance.put(id=2,title="masla dosa",calorie=180)

food_instance.delete(id=1)

food_instance.get()
