total=0
count=0

mark=int(input("enter mark"))

while(mark!=-1):

    total+=mark
    count+=1

    mark=int(input("enter mark"))

if count>0:
    print("total student",count)
    print("average",total/count)