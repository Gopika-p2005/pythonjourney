
trip={
    "anal":2000,
    "aravid":1800,
    "aswin":2500,
    "jithish":750
}

trip["rohan"]=500 # add a new key value pair

trip["anal"]+=1000 # update

trip["aswin"]+=1000

trip["aravid"]-=500

for k in trip:

    print(k,"=>",trip[k])


#total expence

total=0

for k in trip:

    v=trip[k]

    total+=v

print("totatal expence",total)