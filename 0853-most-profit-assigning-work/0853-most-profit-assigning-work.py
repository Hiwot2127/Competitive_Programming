class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        max_prof = 0
        best = 0
        i = 0
        n = len(jobs)
        
        for ab in worker:
            while i < n and jobs[i][0] <= ab:
                best = max(best, jobs[i][1])
                i += 1
            max_prof+= best
        
        return max_prof
        
