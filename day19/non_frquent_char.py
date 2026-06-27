text="pythonprogrammingissimple"
text_count={}

for ch in text:
    if ch in text_count:

        text_count[ch]+=1

    else:

        text_count[ch]=1

for k,v in text_count.items():

    if v==1:

        print(k)

