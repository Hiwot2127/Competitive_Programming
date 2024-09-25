class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashmap={}

        for winner,looser in matches:
            hashmap[winner] = hashmap.get(winner,0)
            hashmap[looser] = 1 + hashmap.get(looser,0)
        
        ans=[[],[]]
        
        for player,loses in hashmap.items():
            if(loses==0):
                ans[0].append(player)
            if(loses==1):
                ans[1].append(player)
        return  [sorted(ans[0]),sorted(ans[1])]