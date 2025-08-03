# 213 - House Robber II
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        def maxMoney(start, end):
            prev = 0
            curr = 0
            for num in nums[start:end]:
                prev_prev = prev
                prev_curr = curr
                prev = prev_curr
                curr = max(prev_curr, prev_prev+num)
            return curr
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(maxMoney(0, n-1), maxMoney(1, n))