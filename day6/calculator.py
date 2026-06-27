number1 = int(input("enter number1.."))
number2 = int(input("enter number2.."))
operation = input("enter operations (+,-,*,/)")

match operation:

    case "+" : print(f"{number1} + {number2} = {number1+number2}")
    case "-" : print(f"{number1} - {number2}  = {number1-number2}")
    case "*" : print(f"{number1}  * {number2} = {number1*number2}")
    case "/" : print(f"{number1} / {number2}= {number1/number2}")

    case _ : print("invalid")