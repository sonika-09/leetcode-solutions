# 78 - Subsets
# Runtime = 0, Beats = 100%

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, pack):
            res.append(pack[:])
            for i in range (start, len(nums)):
                pack.append(nums[i])
                backtrack(i+1, pack)
                pack.pop()
        backtrack(0, [])
        return res