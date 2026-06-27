"""

anonymous function with single expression

"""
#addition
add=lambda num1,num2:num1+num2

print(add(100,200))

#cube of a number
cube=lambda n:n**3

print(cube(3))

#subtraction
sub=lambda num1,num2:num1-num2

print(sub(100,80))

#odd or even
odd_or_even=lambda num:"even" if num%2==0 else "odd"

print(odd_or_even(10))

#write a lambda function to square the number
square=lambda num:num**2

print(square(6))

#write a lambda function to return largest of two number
max_two=lambda n1,n2,:n1 if n1>n2 else n2

print(max_two(100,20))

#min of two number
min_two=lambda n1,n2:n1 if n1<n2 else n2

print(min_two(10,20))