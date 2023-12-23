#given a non-decreasing integer array timeSeries, 
#where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.
#Return the total number of seconds that Ashe is poisoned.

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries or duration == 0:
            return 0
        total_poisoned_time = 0

        for i in range(1, len(timeSeries)):
            time_gap = timeSeries[i] - timeSeries[i-1]
            total_poisoned_time += min(time_gap, duration)

        total_poisoned_time += duration
        return total_poisoned_time