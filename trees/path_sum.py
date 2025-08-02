# 112 - Path Sum
# Runtime = 0ms, Beats = 100%

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.right and not root.left:
            return root.val == targetSum
        
        return (self.hasPathSum(root.right, targetSum-root.val)) or (self.hasPathSum(root.left, targetSum-root.val))
