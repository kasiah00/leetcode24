class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt=0
        for i in range(0,131):
            if x%2+y%2==1:
                cnt+=1
            x=x//2
            y=y//2
        return cnt