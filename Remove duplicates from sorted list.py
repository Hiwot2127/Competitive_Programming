lass Solution(object):
    def deleteDuplicates(self, head):
        last = ListNode(-1)
        last.next = head
        
        curr, prev = head, last
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
                
        return last.next
