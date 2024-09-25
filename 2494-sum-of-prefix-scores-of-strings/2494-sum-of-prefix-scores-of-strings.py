class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def calculate(self, word):
        node = self.root
        score = 0
        for char in word:
            node = node.children[char]
            score += node.count
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        res = []
        for word in words:
            trie.insert(word)
        for word in words:
            score = trie.calculate(word)
            res.append(score)
        return res
