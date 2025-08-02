# 53 - Maximum Subarray
# Runtime = 248ms, Beats = 5.06%

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        memo = [-1] * (n)
        def maxSub(n):
            if(n == 0):
                return nums[0]
            elif(n == 1):
                return max(nums[1], nums[0]+nums[1])
            if(memo[n] != -1):
                return memo[n]
            memo[n] = max(nums[n], maxSub(n-1)+nums[n])
            return memo[n]
        maxSum = nums[0]
        for i in range(n):
                maxSum = max(maxSum, maxSub(i))
        return maxSum
        