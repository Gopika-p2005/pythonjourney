note="dam"

magazin="madam"

container_word=True

for ch in note:

    if magazin.find(ch)==-1:

        container_word=False

        break


print(container_word)
