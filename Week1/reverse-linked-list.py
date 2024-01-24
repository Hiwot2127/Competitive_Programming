# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Nlist= None
        cur= head

        while cur:
            next=cur.next
            cur.next=Nlist
            Nlist=cur
            cur=next
        return Nlist


        