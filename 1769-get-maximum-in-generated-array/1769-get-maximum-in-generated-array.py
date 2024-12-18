class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n: return n
        n_2, n_1 = 0, 1
        res = 1
        for _ in range(n - 1):
            n_2, n_1 = n_1, n_1 + n_2 - 2 * (n_2 % n_1)
            res = max(res, n_1)
        return res