# 39 - Combination Sum
# Runtime = 15ms, Beats = 27.91%

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()	# just makes elimination easier 
        def uniqueComb(start, path, total):
            if(total == target):
                res.append(path[:])
                return
            elif(total > target):
                return
            for i in range (start, len(candidates)):
                path.append(candidates[i])
                uniqueComb(i, path, total+candidates[i])
                path.pop()
        uniqueComb(0, [], 0)
        return res