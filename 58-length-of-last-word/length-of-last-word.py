class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed_s = s.strip()
        length = 0

        for char in trimmed_s[::-1]:
            if char == ' ':
                if length != 0:
                    return length
            else:
                length += 1

        return length