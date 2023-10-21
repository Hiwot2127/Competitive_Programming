class Solution:
    def reverse(self, x: int) -> int:
        new=abs(x)
        num=0

        while new:
            num=num*10 + new % 10
            new= new//10

        num= num if x==abs(x) else num*-1

        return num if num>-2**31 and num<2**31-1 else 0
