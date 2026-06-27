total_classes = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = (attended / total_classes) * 100

print("Attendance Percentage:", percentage)

if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")