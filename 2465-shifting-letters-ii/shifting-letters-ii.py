class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        prefix = [0] * (len(s)+1)

        for start, end, direct in shifts:
            counter = 1 if direct == 1 else -1
            prefix[start]+=counter
            prefix[end+1]-=counter

        for i in range(1, len(prefix)):
            prefix[i]+=prefix[i-1]

        res = ""

        for i in range(len(s)):
            new_val = (ord(s[i]) + prefix[i]%26)

            if 97 <= new_val <= 122:
                res+=chr(new_val)
            elif new_val > 122:
                res+=chr(new_val%123 + 97)
            else:
                res+=chr(new_val+26)
        return res
        