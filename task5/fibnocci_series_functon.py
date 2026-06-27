def fibnocci(num):
    num1=0
    num2=1
    count=0

    while(count<num):
    
        sum=num1+num2
    
        num1=num2

        num2=sum

        count+=1
    print(num1)
        
    


fibnocci(6)