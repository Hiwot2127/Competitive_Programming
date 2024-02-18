# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        num_per_part, remainder = divmod(length, k)
        
        result = []
        curr = head
        for i in range(k):
            result.append(curr)
            part_size = num_per_part + (1 if i < remainder else 0)
            if part_size > 0:
                for _ in range(part_size - 1):
                    curr = curr.next
                temp = curr.next
                curr.next = None
                curr = temp
        return result