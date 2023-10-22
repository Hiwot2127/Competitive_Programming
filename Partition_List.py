# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur=head
        lessd=ListNode(0)
        lesst=lessd

        greatd=ListNode(0)
        greatt=greatd

        while cur:
            if cur.val<x:
                lesst.next=ListNode(cur.val)
                lesst=lesst.next
            else:
                greatt.next=ListNode(cur.val)
                greatt=greatt.next
            cur= cur.next
        lesst.next= greatd.next
        return lessd.next
