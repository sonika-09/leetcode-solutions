# 647 - Palindromic Substrings
# Runtime = 142ms, Beats = 89.60%

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        result = 0
        def isPalindrome(left, right):
            count = 0
            while(left>=0 and right<n and s[left]==s[right]):
                count += 1
                left -= 1
                right += 1
            return count
        for i in range(n):
            result += isPalindrome(i, i)
            result += isPalindrome(i, i+1)
        return result