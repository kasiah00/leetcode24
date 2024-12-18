class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        flush=list(set(suits))
        if len(flush)==1:
            return "Flush"
        body={
            3:"Three of a Kind",
            2:"Pair",
            1:"High Card",
        }
        k={}
        for i in sorted(set(ranks)):
            count=ranks.count(i)
            k[i]=count
        kl=sorted(k.items(),key=lambda x:x[1])
        print(kl[-1])
        pl=kl[-1]
        print(pl)
        if pl[1]>=3:
            return body[3]
        elif pl[1]==2:
            return body[2]
        return body[1]
