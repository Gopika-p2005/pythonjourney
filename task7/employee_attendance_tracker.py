present = 0
absent = 0

for i in range(30):
    status = input("P/A: ")

    if status == "P":
        present += 1
    else:
        absent += 1

print("Present:", present)
print("Absent:", absent)