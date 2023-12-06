class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        i = 0
        minlength= min(len(word1), len(word2))

        while i < minlength:
            res+= word1[i]+word2[i]
            i+=1
        while i<len(word1):
            res+=word1[i]
            i+=1
        while i<len(word2):
            res+=word2[i]
            i+=1
        return res   
            