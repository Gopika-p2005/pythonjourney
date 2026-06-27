product_dic={"id":101,"title":"shoes","price":1200,"category":"fancy"}

for k in product_dic:

    print(k ,"=>" ,product_dic[k])

product_dic["price"]=1250 #update

print(product_dic)

product_dic["brand"]="nike" #add a new key value pair

print(product_dic)

#print(product_dic["category"])

#print(product_dic["price"])

