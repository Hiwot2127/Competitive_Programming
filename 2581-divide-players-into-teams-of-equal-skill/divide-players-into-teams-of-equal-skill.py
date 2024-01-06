class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        p = []
        f = []
        while l< len(skill)/2:
            p.append(skill[l] * skill[r])
            f.append(skill[l] + skill[r])
            l+=1
            r-=1
        if len(set(f))==1:
            return (sum(p))
        else:
            return (-1)