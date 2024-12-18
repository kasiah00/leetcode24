class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            x=max(gifts)
            gifts.remove(x)
            gifts.append(int(sqrt(x)))
        return sum(gifts)