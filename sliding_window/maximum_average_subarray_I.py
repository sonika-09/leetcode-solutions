# 643 - Maximum Average Subarray I
# Runtime = 45ms, Beats = 90.11%

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i-k]
            if max_sum < curr_sum:
                max_sum = curr_sum
        return float(max_sum) / k
