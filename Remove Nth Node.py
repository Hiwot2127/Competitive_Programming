# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = cur = a = ListNode(0, head)
        len = 0

        while cur:
            len+=1
            cur=cur.next
        point = len-n

        cur = start
        for i in range(point-1):
            a = a.next
            cur = cur.next
        a = a.next.next
        cur.next = a

        return start.next        
