class Solution:
    def minimumPushes(self, word: str) -> int:
        let_counts = {}
        for c in word:
            let_counts[c] = let_counts.get(c, 0) + 1
        counts = list(let_counts.values())
        counts.sort(reverse=True)
        ans, row = 0, 1
        for i in range(len(counts)):
            if i > 7 and i % 8 == 0:
                row += 1
            ans += row * counts[i]
        return ans