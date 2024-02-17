class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        length = 0
        hasOdd = False

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                hasOdd = True

        if hasOdd:
            length += 1

        return length
            