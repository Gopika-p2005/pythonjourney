def mark_calculate(mark1,mark2,mark3,mark4):

    avg=(mark1+mark2+mark3+mark4)/4

    if mark1<40 or mark2<40 or mark3<40 or mark4<40:

        print("fail")

    elif avg>=60:

        print("first class")

    elif avg>=75:

        print("distinction")


    else:
        print("fail")

mark_calculate(34,55,67,87)
mark_calculate(44,55,67,87)