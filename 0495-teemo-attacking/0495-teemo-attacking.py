class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time = 0

        for i in range(len(timeSeries) - 1):
            time += min(duration, timeSeries[i + 1] - timeSeries[i])

        return time + duration