class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=str(n)
        add=0
        mul=1
        for i in s:
            add+=int(i)
            mul*=int(i)
        return mul-add
