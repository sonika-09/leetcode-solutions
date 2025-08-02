# 268 - Missing Number
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSize = len(nums)
        expectedSum = (numsSize * (numsSize+1)) / 2
        obtainedSum = sum(nums)
        return expectedSum-obtainedSum