def digit_count(text):

    count=0

    for ch in text:

        if ch.isdigit():

            count+=1

    return count


print(digit_count("abc123"))
print(digit_count("abc"))