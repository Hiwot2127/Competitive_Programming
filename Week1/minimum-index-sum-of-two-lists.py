class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idict = {}
        res = []
        msum = float('inf')

        for i, word in enumerate(list1):
            idict[word] = i

        for j, word in enumerate(list2):
            if word in idict:
                csum = j + idict[word]
                if csum < msum:
                    res = [word]
                    msum = csum
                elif csum == msum:
                    res.append(word)

        return res