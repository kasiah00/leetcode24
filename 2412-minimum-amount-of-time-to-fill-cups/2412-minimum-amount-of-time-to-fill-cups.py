class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        cnt=0
        while amount[0]>0:
            if amount[1]>0:
                amount[0]-=1
                amount[1]-=1
                cnt+=1
                amount.sort(reverse=True)
            else:
                amount[0]-=1
                cnt+=1
        return cnt