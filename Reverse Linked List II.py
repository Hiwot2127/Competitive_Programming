# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head and left == right:
            return head

        rev = ListNode(0, head)
        prev = rev

        for i in range(left - 1):
            prev = prev.next

        tail = prev.next

    
        for i in range(right - left):
            cache = tail.next
            tail.next = cache.next
            cache.next = prev.next
            prev.next = cache

        return rev.next
