# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
        size = l // k
        extra = l % k
        res = []
        temp = head
        
        for i in range(k):
            if not temp:
                res.append(None) 
            else:
                res.append(temp)
                c = size + 1 if extra > 0 else size
                extra -= 1
                for j in range(c - 1):
                    temp = temp.next  
                next_node = temp.next
                temp.next = None  
                temp = next_node  
        return res