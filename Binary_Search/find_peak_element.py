# 162 - Find Peak Element
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        while (right > left):
            mid = (left+right) // 2
            if(nums[mid] > nums[mid+1]):    # peak is towards the left
                right = mid
            else:
                left = mid+1
        return left