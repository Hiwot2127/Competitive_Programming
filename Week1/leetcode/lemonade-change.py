class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        Five=0
        Ten=0
        Twenty=0

        for i in range(len(bills)):
            if bills[i]==5:
                Five+=1
            elif bills[i]==10:
                Ten+=1
                if Five>0:
                    Five-=1
                else:
                    return False
            else: 
                if Ten>0 and Five>0:
                    Ten-=1
                    Five-=1
                elif Five>2:
                    Five-=3
                else:
                    return False
        return True
                
