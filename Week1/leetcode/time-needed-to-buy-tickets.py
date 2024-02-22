class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n=len(tickets)
        q=deque([i for i in range(n)])
        time=0
        
        while q:
            for i in range(len(q)):

                ppl=q.popleft()
                tickets[ppl]-=1

                if tickets[ppl]>=1:
                    q.append(ppl)
                time+=1

                if tickets[k]==0:
                    return time
                
                
        