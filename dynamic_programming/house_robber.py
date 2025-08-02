# 198 - House Robber
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        curr = 0
        for num in nums:
            prev_prev = prev
            prev_curr = curr
            prev = curr
            curr = max(prev_curr, prev_prev + num)
        return curr