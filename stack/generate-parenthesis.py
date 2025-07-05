# 22 - Generate Parenthesis
# Runtime = 0ms, Beats = 100%

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_counter, close_counter):
            if(len(current) == 2*n):    # the combination has been made, so we stop adding elements to it and return
                result.append(current)
                return
            if(open_counter < n):    # number of opening parenthesis should always be less than or equal to given number
                backtrack(current + '(', open_counter+1, close_counter)
            if(close_counter < open_counter):    # at any point, there shouldn't be more closing parenthesis than opening
                backtrack(current + ')', open_counter, close_counter+1)
        
        backtrack('', 0, 0)
        return result
