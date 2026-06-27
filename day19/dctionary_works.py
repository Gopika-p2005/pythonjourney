roman={
    "I":1,
    "v":5,
    "X":10,
    "L":50,
}

roman["C"]=100

roman["D"]=500

roman["M"]=1000



print("key")

for k in roman.keys():
    print(k)


print("value")

for v in roman.values():
    
    print(v)


print("key and value")

for k,v in roman.items():

    print(k,v)
