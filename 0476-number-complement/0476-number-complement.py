class Solution:
    def findComplement(self, num: int) -> int:
            res=bin(num)
            new=''
            for i in res[2:]:
                if i=='0':
                    new+='1'
                elif i=='1':
                    new+='0'
            return int(new,2)