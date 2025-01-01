class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=Counter(ransomNote)
        m=Counter(magazine)
        for i,st in enumerate(ransomNote):
            if st in magazine and r[st]<=m[st]:
                continue
            else:
                return False
        return True
            
