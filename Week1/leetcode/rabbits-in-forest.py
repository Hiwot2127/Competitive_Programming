class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        res = 0
        
        for ans in answers:
            if ans not in count:
                count[ans] = 0
            count[ans] += 1
        
        for ans, rabbits in count.items():
            grps = rabbits // (ans + 1)
            if rabbits % (ans + 1) != 0:
                grps += 1
            res += grps * (ans + 1)
        
        return res