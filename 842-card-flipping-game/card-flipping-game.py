class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        good_integers = set(fronts) | set(backs)

        for i in range(n):
            if fronts[i] == backs[i]:
                good_integers.discard(fronts[i])

        return min(good_integers) if good_integers else 0