class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(p): 
            if parent[p] != p: 
                parent[p] = find(parent[p])
            return parent[p]
        
        for p, q in edges: 
            prt, qrt = find(p), find(q)
            if prt != qrt: parent[prt] = qrt
        
        freq = Counter(find(p) for p in range(n))
        return sum(v*(n-v) for v in freq.values())//2