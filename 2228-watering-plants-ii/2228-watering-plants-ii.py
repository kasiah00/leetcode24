class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        A=capacityA
        B=capacityB
        cnt=0
        i,j=0,len(plants)-1
        while i<=j :
            if i==j :
                if A < plants[i] and B < plants[j] :
                    cnt+=1
            else :
                if A >=plants[i] :
                    A -=plants[i]
                else :
                    cnt +=1
                    A = capacityA -plants[i]
                if B >= plants[j] :
                    B -=plants[j]
                else :
                    cnt += 1
                    B = capacityB - plants[j]
            i+=1
            j-=1
        return cnt