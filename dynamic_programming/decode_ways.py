# 91 - Decode Ways
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = [-1] * n
        def decoder(i):
            if(i == len(s)):
                return 1
            if(s[i] == '0'):
                return 0
            if memo[i] != -1:
                return memo[i]
            ways = decoder(i+1)

            if((i+1 < len(s)) and 10 <= int(s[i:i+2]) <= 26):
                ways += decoder(i+2)
            memo[i] = ways
            return ways
        return decoder(0)