numbers=[2,3,4,5,6,7,8]

#evens=[return_value iteration condition]

evens=[num for num in numbers if num%2==0]

print(evens)

odds=[num for num in numbers if num%2!=0]

print(odds)
