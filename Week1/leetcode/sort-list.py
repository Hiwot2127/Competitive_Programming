# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getmid(head):
            slow,fast=head,head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        def merge(left_half,right_half):
            tail=dummy=ListNode()
            while left_half and right_half:
                if left_half.val<right_half.val:
                    tail.next=left_half
                    left_half=left_half.next
                else:
                    tail.next=right_half
                    right_half=right_half.next
                tail=tail.next
            if left_half:
                tail.next=left_half
            if right_half:
                tail.next=right_half
            return dummy.next

        if not head or head.next is None:
            return head
            
        left=head
        right=getmid(head)
        tmp=right.next
        right.next=None
        right=tmp

        left=self.sortList(left)
        right=self.sortList(right)
        return merge(left,right)
