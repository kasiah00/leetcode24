class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [
            x[0] for x in sorted(enumerate(map(sum, mat)), key=lambda x: x[::-1])
        ][:k]