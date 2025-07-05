# 150 - Evaluate Reverse Polish Notation
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if (c=='+' or c=='-' or c=='*' or c=='/'):
                ele1 = stack.pop()    # we pop 2 elements to perform the operation
                ele2 = stack.pop()
                if(c=='+'):
                    stack.append(ele2 + ele1)
                elif(c=='-'):
                    stack.append(ele2 - ele1)
                elif(c=='*'):
                    stack.append(ele2 * ele1)
                else:
                    stack.append(int(ele2/ele1))    # the result of division should not be a float
            else:
                stack.append(int(c))    # to be able to push operations, we need to convert these strings into integers
        return stack[-1]
        
