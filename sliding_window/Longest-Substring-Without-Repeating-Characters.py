//3 - Longest Substring Without Repeating Characters
//Runtime = 23ms, Beats = 61.82%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        seen = {}
        max_length=0
        for i in range(len(s)):
            if(s[i] in seen and seen[s[i]] >= start):
                start = seen[s[i]] + 1
            seen[s[i]] = i
            max_length = max(max_length, i-start+1)
        return max_length
        