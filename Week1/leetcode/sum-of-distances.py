class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        track={}
        for i in range (len(nums)):
            if nums[i] not in track:
                track[nums[i]]=[]
                track[nums[i]].append(i)
            else:
                track[nums[i]].append(i)

        res=[0]*(len(nums))
        for key,val in track.items():
            suff=sum(val)
            pre=0
            s=len(val)
            p=0
            for i in val:
                pre+=i 
                p+=1
                suff-=i
                s-=1
                res[i]=(-pre+p*i-s*i+suff)
        return res
        