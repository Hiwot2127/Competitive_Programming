class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res=[]
        i=0
        for i in range(len(words)):
            first, second, third = 0, 0 , 0

            for char in words[i]:
                char = char.lower()
                if char in "qwertyuiop":
                    first+=1
                elif char in "asdfghjkl":
                    second+=1
                elif char in "zxcvbnm":
                    third+=1
            if first>0 and second==0 and third==0:
                res.append(words[i])
            elif first==0 and second>0 and third==0:
                res.append(words[i])
            elif first==0 and second==0 and third>0:
                 res.append(words[i])
        
        return res
        


            