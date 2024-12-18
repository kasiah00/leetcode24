class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res=[]
        for i in range(len(t)):
            first=i
            ind=s.index(t[i])
            res.append(abs(first-ind))
        return sum(res)