class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        box = [0] * k
        for n in arr:
            r = (n % k + k) % k
            box[r] += 1
        if box[0] % 2 != 0:
            return False
        for i in range(1,k//2+1):
            if box[i]!=box[k-i]:
                return False
        return True
