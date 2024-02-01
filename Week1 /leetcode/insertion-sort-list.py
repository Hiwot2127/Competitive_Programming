# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head = ListNode(float('-inf'))  
        current = head

        while current:
            next_node = current.next  
            prev = sorted_head
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            current.next = prev.next
            prev.next = current

            current = next_node  

        return sorted_head.next 