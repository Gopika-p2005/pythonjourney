#text="hello! world python123"

def character_count(text):

    count=0

    for ch in text:

        if ch.isalnum():

            count+=1

    return count

print(character_count("hello! world python123"))