class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
       track= set()
       for start,end in ranges:
            for i in range(start, end+1):
                track.add(i)

       for j in range(left, right+1):
            if j not in track:
                return False
       return True
        

            

           
           