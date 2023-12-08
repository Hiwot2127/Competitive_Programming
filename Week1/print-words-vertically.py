class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(len(word) for word in words)
        res = []

        for i in range(max_length):
            column = ""
            for word in words:
                if i < len(word):
                    column += word[i]
                else:
                    column += " "
            res.append(column.rstrip()) 
        return res
