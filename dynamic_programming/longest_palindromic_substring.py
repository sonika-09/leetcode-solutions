# 5 - Longest Palindromic Substring
# Runtime = 281ms, Beats = 95.985

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        def subStr(left, right):
            while(left >= 0 and right<n and s[left]==s[right]):
                left -= 1
                right += 1
            return s[left+1:right]
        longest = ""
        for i in range(n):
            temp1 = subStr(i, i) # odd length
            temp2 = subStr(i, i+1) # even length
            if (len(temp1) > len(longest)):
                longest = temp1
            if(len(temp2) > len(longest)):
                longest = temp2
        return longest