class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lp = 0
        hp = len(people)-1
        boats = 0

        while lp <= hp:
            if people[lp] + people[hp] <= limit:
                lp += 1
                hp -= 1
            else:
                hp -= 1
            boats += 1
            
        return boats