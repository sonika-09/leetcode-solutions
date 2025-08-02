# 33 - Search in Rotated Sorted Array
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        while(left <= right):
            mid = (right+left) // 2
            if(nums[mid] == target):
                return mid
            if(nums[left] <= nums[mid]):
                if(nums[left] <= target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if(nums[mid] < target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
        return -1