def character_count(text):


    count=0

    for ch in text:

        if ch.isalpha():

            count+=1

    return count


print(character_count("hello world"))
print(character_count("hello python"))
