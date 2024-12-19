class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for _ in range(k):
            smallest = min(nums)
            idx_small = nums.index(smallest)
            nums[idx_small] = -smallest
        return sum(nums)