"""
item_price =950
quantity = 5
discount = 8% on total price

delivery_charge = 47

find final amount
"""


item_price = 950

qunantity =5

delivery_charge = 47

total_price = item_price * qunantity

discount = (8/100)*total_price

discount_price = total_price - discount

final_price = discount_price + delivery_charge

print("final price", final_price)