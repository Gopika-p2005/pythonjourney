word="helloo"

printed=[]

for ch in word:

    if word.count(ch)>1 and ch not in printed:
    

        print(ch)

        printed.append(ch)