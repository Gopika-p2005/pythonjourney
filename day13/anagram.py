word1="earth"

word2="heart"

anagram=True

for ch in word1:

    if word1.count(ch) != word2.count(ch):

        anagram=False

        break

print(anagram)
