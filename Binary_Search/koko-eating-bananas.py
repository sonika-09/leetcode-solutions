# 875 - Koko Eating Bananas
# Runtime = 156ms, Beats = 58.46%

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 # lowest value that k could be
        high = max(piles)   # highest value that k could be
        result = high   # initial setting
        while (high >= low):
            k = (high+low)//2   # binary search
            hours_count = sum(ceil(value/k) for value in piles) # adds up the hours each pile takes to be eaten with speed k
            if (hours_count <= h):
                result = k  # not the final answer yet
                high = k - 1    # because we need to find minimum value for k
            else:
                low = k + 1
        return result

# stepped a lil closer to insanity with this one
