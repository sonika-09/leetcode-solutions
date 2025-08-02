# 844 - Backspace String Compare
# Runtime = 4ms, Beats = 16.69%

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def strCompare(temp):
            stack = []
            for char in temp:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        return strCompare(s) == strCompare(t)
        