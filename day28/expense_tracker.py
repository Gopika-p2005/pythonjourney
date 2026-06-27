#ExpenseTracker[name,phone,email,transaction:[{},{}],add_transaction(),list_transaction(),summary()]


class ExpenseTracker:

    def __init__(self,name,phone,email):

        self.name=name

        self.phone=phone

        self.email=email

        self.transaction=[]

    def add_transaction(self,name=None,amount=None,category=None):

        self.transaction.append({"name":name,"amount":amount,"category":category})

    def list_transaction(self):

        print(self.transaction)

    def summary(self):

        all_amount=[amount["amount"] for amount in self.transaction ]

        print("total amount",sum(all_amount))

        category_summary={}

        for cash in self.transaction:

            category=cash["category"]

            amount=cash["amount"]

            if category in category_summary:

                category_summary[category]+=amount

            else:

                category_summary[category]=amount

        print("category amount summary",category_summary)


amount_instance1=ExpenseTracker("ranju",90876383,"ranju786.@gmail.com")


amount_instance1.add_transaction(name="bus",amount=450,category="transportation")
amount_instance1.add_transaction(name="movie",amount=180,category="entertainment")
amount_instance1.add_transaction(name="bakery",amount=500,category="food")
amount_instance1.add_transaction(name="bakery",amount=540,category="food")
amount_instance1.add_transaction(name="mobile",amount=350,category="recharge")

amount_instance1.list_transaction()

amount_instance1.summary()
