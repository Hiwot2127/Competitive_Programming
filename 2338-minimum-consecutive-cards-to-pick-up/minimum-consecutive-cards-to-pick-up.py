class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        Hash={}
        length=[]

        for i,j in enumerate(cards):
            if j in Hash:
                length.append(abs(Hash[j]-i)+1)
                Hash[j]=i
            else:
                Hash[j]=i
        if len(length)>0:
            return min(length)
        else:
            return -1