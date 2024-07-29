# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currSum = 0
        flag = head
        temp = head.next

        while temp:
            if temp.val == 0:
                node = ListNode(currSum)
                flag.next = node
                flag = node
                currSum = 0
            else:
                currSum += temp.val
            temp = temp.next
        return head.next