class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        if k<numOnes:
            return k
        if k<numOnes+numZeros:
            return numOnes
        k-=numOnes+numZeros
        return numOnes-k
            