class Anagram:

    def solution(self,word1,word2):

        print(sorted(word1)==sorted(word2))

ang=Anagram()

ang.solution("listen","silent")

ang.solution("hen","chicken")