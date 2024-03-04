class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        rad_count = senate.count('R')
        dir_count = len(senate) - rad_count
        rad_banned = dir_banned = 0
        while rad_banned < rad_count and dir_banned < dir_count:
            senator = queue.popleft()
            if senator == 'R':
                if rad_banned > 0:
                    rad_banned -= 1
                else:
                    queue.append('R')
                    dir_banned += 1
            else:
                if dir_banned > 0:
                    dir_banned -= 1
                else:
                    queue.append('D')
                    rad_banned += 1

        return 'Radiant' if dir_count == dir_banned else 'Dire'