class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = str(num)
        num_list = list(nums)

        if num==0: 
            return 0
        if num_list[0] == '-':
            sorted_digits = sorted(num_list[1::],reverse=True)
            result = "-" + "".join(sorted_digits)
        else:
            sorted_digits = sorted(num_list)
            i=1
            while (sorted_digits[0]=='0'):  
                sorted_digits[0]=sorted_digits[i] 
                sorted_digits[i]=0
                i+=1
            result = "".join(map(str,sorted_digits))

        return int(result)