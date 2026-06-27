class DietLines:

    def __init__(self,name,age,weight,height,gender):

        self.name=name

        self.age=age

        self.weight=weight

        self.height=height

        self.gender=gender

        self.food_logs=[]

    def add_food_logs(self,name=None,calorie=None,meal_type=None):

        self.food_logs.append({"name":name,"calorie":calorie,"meal_type":meal_type})

    def list_food_logs(self):

        print(self.food_logs)

    def summary(self):

        all_calories=[log["calorie"] for log in self.food_logs]

        print("total calorie",sum(all_calories))

        meal_summary={}

        for log in self.food_logs:

            meal_type=log["meal_type"]

            calorie=log["calorie"]

            if meal_type in meal_summary:

                meal_summary[meal_type]+=calorie

            else:

                meal_summary[meal_type]=calorie

        print("meal type summary",meal_summary)

diet_lines_instance1=DietLines("abhi",22,56,156,"male")


diet_lines_instance1.add_food_logs(name="puttu",calorie=156,meal_type="break_fast")
diet_lines_instance1.add_food_logs(name="meal",calorie=220,meal_type="lunch")
diet_lines_instance1.add_food_logs(name="shake",calorie=120,meal_type="evening")
diet_lines_instance1.add_food_logs(name="fried rice",calorie=180,meal_type="dinner")

diet_lines_instance1.list_food_logs()

diet_lines_instance1.summary()
