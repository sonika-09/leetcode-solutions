// 22 - Generate Parenthesis
// Runtime = 0ms, Beats = 100%

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_counter, close_counter):
            if(len(current) == 2*n):
                result.append(current)
                return
            if(open_counter < n):
                backtrack(current + '(', open_counter+1, close_counter)
            if(close_counter < open_counter):
                backtrack(current + ')', open_counter, close_counter+1)
        
        backtrack('', 0, 0)
        return result