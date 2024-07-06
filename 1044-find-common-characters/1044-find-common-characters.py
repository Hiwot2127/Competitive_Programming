class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words
        ans = []
        word1 = set(words[0])
        for char in word1:
            frequency = min([word.count(char) for word in words])
            ans += [char] * frequency
        return ans