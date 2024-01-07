class Solution:
    def findAnagrams(self, string: str, anagram: str) -> List[int]:
        
        anagram = ''.join(sorted(anagram))
        window_string = ''
        res = []
        window_start = 0
        
        for char in string:
            window_string += char
        
            if len(window_string) == len(anagram):
                if ''.join(sorted(window_string)) == anagram:
                    res.append(window_start)
                
                window_string = window_string[1:]
                window_start += 1

        return res
    