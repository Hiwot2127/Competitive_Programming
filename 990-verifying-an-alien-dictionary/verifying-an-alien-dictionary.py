class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        track = {char: i for i, char in enumerate(order)}
        prev = list(track[char] for char in words[0])

        for i in range(1, len(words)):
            cur = list(track[ch] for ch in words[i])
            if cur < prev:
                return False
            prev = cur
        return True