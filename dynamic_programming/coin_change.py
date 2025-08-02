# 322 - Coin Change
# Runtime = 1362ms, Beats = 17.78%

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # amount+1 => largest value
        memo = {}
        def check(amt):
            if(amt == 0):
                return 0
            elif(amt < 0):
                return amount+1
            if(amt in memo):
                return memo[amt]
            min_coin = amount+1
            for coin in coins:
                result = check(amt - coin)
                if result != amount+1:
                    min_coin = min(min_coin, result+1)
            memo[amt] = min_coin
            return memo[amt]
        ans = check(amount)
        return ans if (ans != amount+1) else -1