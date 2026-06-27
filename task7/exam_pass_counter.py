pass_count = 0
fail_count = 0

for i in range(20):
    marks = int(input("Enter marks: "))

    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1

print("Pass:", pass_count)
print("Fail:", fail_count)