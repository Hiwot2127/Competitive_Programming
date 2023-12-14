class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        lost= set()
        count = {}

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            lost.add(loser)
            count[loser] = count.get(loser, 0) + 1

        no = sorted(list(players - lost))
        one = sorted([player for player in count if count[player] == 1])

        return [no, one]
