class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        cs1 = Counter(s1)
        
        for i in range(len(s2)-window+1):

            cs2 = Counter(s2[i:i+window])

            if cs2 == cs1:
                return True
            
        return False