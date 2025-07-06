# 155 - Min Stack
# Runtime = 0ms, Beats = 100%

class MinStack(object):

    def __init__(self):
        self.stack = []    # for regular operation
        self.min_ele = []    # for minimum element

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_ele or val <= self.min_ele[-1]:    # if value pushed is lesser than top element of min_ele then push
            self.min_ele.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if((len(self.min_ele)>0) and (self.stack[-1] == self.min_ele[-1])):    # checks if minimum element is being popped
            self.min_ele.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if(len(self.min_ele)>0):
            return self.min_ele[-1]
        else:
            return None
        
