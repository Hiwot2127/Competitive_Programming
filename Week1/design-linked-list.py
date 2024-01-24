class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        cur=self.head
        count=0
        while cur and count!=index:
            cur=cur.next
            count+=1
        if not cur:
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new=Node(val)
        new.next=self.head
        self.head=new

    def addAtTail(self, val: int) -> None:
        last=Node(val)
        if not self.head:
            self.head=last
            return 
        last1=self.head
        while last1.next:
            last1=last1.next
        last1.next=last

    def addAtIndex(self, index: int, val: int) -> None:
        tmp= Node(val)
        if index==0:
            tmp.next=self.head
            self.head=tmp
            return
        tmp1=self.head
        prev1= None
        count=0
        while tmp1 and count!=index:
            prev1=tmp1
            tmp1=tmp1.next
            count+=1
        if not prev1:
            return
        prev1.next=tmp
        tmp.next=tmp1 
  

    def deleteAtIndex(self, index: int) -> None:
        pin=self.head
        if index==0:
            self.head=pin.next
            pin=None
            return
        prev=None
        count=0
        while pin and count!=index:
            prev=pin
            pin=pin.next
            count+=1
        if not pin:
            return
        prev.next=pin.next
        pin = None



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)