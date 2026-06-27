expenses=[870,670,780,1200,1300,1400,870]

total=0

for exp in expenses:


    total+=exp

print("total exp",total)

avg=total/len(expenses)

print("avg",avg)

print("=============================")

for exp in expenses:

    if exp>avg:

        print(exp)

print("======================================")

costly_exp=expenses[0]

for exp in expenses:

    if exp>costly_exp:

        costly_exp=exp

print("costly expense",costly_exp)

print("=========================")

cheepest_exp=expenses[0]

for exp in expenses:

    if exp<cheepest_exp:

        cheepest_exp=exp

print("cheepest expenses",cheepest_exp)

