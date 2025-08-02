# 283 - Move Zeroes
# Runtime = 3ms, Beats = 88.79%

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in nums:
            if i != 0:
                nums[pos] = i
                pos += 1
        for j in range(pos, len(nums)):
            nums[j] = 0