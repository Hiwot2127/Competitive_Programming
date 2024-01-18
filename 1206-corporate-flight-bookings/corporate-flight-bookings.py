class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix=[0]*(n+2)

        for first,last,seats in bookings:
            prefix[first]+=seats
            print(prefix[first])
            prefix[last+1]-=seats

        for i in range(1,len(prefix)):
            prefix[i]+=prefix[i-1]
        prefix.remove(prefix[0])
        prefix.pop()
        return prefix





