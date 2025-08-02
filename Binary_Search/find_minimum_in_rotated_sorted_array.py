# 153 - Find Minimum in Rotated Sorted Array
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)

# OR
# Runtime = 3ms, Beats = 6.74%

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        while (right > left):
            mid = (left+right) // 2
            if(nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid
        return nums[left]