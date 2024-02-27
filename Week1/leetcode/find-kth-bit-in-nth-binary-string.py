class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def bit(n):
            if n==1:
                return '0'
            cur=''
            prev=''
            inv=''
            prev=bit(n-1)
            for i in range(len(prev)):
                if prev[i]=='0':
                    inv+='1'
                else:
                    inv+='0'
            cur= prev+'1'+inv[::-1]
            return cur
        print(bit(n))
        res=bit(n)
        return res[k-1]   

