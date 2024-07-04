class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lev1 = version1.split('.')
        lev2 = version2.split('.')
        length = max(len(lev1), len(lev2))

        for i in range(length):
            v1 = int(lev1[i]) if i < len(lev1) else 0
            v2 = int(lev2[i]) if i < len(lev2) else 0
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        return 0