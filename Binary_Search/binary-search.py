# 704 - Binary Search
# Runtime = 0ms, Beats = 100%

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bettersearch(nums, target, high, low):
            while(high >= low):
                mid = (high+low)//2
                if(target == nums[mid]):
                    return mid
                elif(target < nums[mid]):
                    high = mid-1	# used iterative, cuz it's faster than recursive
                else:
                    low = mid + 1
            return None
        found = bettersearch(nums, target, len(nums)-1, 0)
        if(found != None):
            return found
        else:
            return -1