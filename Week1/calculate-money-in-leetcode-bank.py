class Solution:
    def totalMoney(self, n: int) -> int:
       list1=[1,2,3,4,5,6,7]
       balance=0
       if n<7:
           for x in range(n):
               balance+=list1[x]
       else:
            no_w=n//7
            R=n%7
            for y in range(no_w):
                balance+=(28+(y*7))

            for x in range(n%7):
                balance+=(list1[x]+no_w)
       return balance