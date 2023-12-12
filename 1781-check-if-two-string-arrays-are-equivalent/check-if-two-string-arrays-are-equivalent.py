class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        conc_word1 = ''.join(word1)
        conc_word2 = ''.join(word2)

        return conc_word1 == conc_word2
