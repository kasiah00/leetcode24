class Solution:
    def checkRecord(self, s: str) -> bool:
        abs=0
        late=0
        for i in s:
            if i=='A':
                abs+=1
                late=0
            elif i=='L':
                late+=1
                if late>2: return False
            else:
                late=0
        if abs>1: return False
        return True