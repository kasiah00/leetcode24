class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high-low)==1:
            return 1
        elif (low%2+high%2)==0:
            return int((high-low)/2)
        else :
            return int((high-low)/2+1)