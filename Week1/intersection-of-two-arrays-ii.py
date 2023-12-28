class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       dict1=Counter(nums1)
       dict2=Counter(nums2)
       res=[]

       for num in dict1.keys() and dict2.keys():
                track= min(dict1[num], dict2[num])
                res.extend([num]*track)
       return res

       