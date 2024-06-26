# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head :
            return head
       
        cur = head
        l = 1  

        while cur.next:
            cur = cur.next
            l += 1
        rot = k % l
        cur.next = head 

        new_tail = head
        for i in range(l-rot-1):
            new_tail = new_tail.next

        res = new_tail.next
        new_tail.next = None 
      
        return res
        