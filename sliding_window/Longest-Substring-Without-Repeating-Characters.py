# 3 - Longest Substring Without Repeating Characters
# Runtime = 23ms, Beats = 61.82%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0    # tracks beginning to current substring
        seen = {}    # dictionary to track last "seen" positions
        max_length=0    # updates when new valid window is found
        for i in range(len(s)):
            if(s[i] in seen and seen[s[i]] >= start):    # duplicate found
                start = seen[s[i]] + 1    # move start after the duplicate
            seen[s[i]] = i    # update last seen index
            max_length = max(max_length, i-start+1)
        return max_length
        
