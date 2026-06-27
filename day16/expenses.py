expenses=[12000,13000,14000,15000,16000]

#display all expenses  13.5k

print("amount > 13.5k")

for amount in expenses:

    if amount > 13500:

        print(amount)


print("==============")
print("amount < 14k")

for cash in expenses:

    if cash < 14000:

        print(cash)


print("====================================" )

print("display all expenses bw 12k to 15k")

for amount in expenses:

    if amount>=12000 and amount<=15000:

        print(amount)

