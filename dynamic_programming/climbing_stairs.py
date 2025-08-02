# 70 - Climbing Stairs
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [-1] * (n+1)
        def climb(rem):
            if rem < 0:
                return 0
            if rem == 0:
                return 1
            if memo[rem] != -1:
                return memo[rem]
            memo[rem] = climb(rem - 1) + climb(rem - 2)
            return memo[rem]
        return climb(n)