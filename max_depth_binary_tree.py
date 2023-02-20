#https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        # edge case
        if not root:
            return 0
        
        max_depth = float('-inf')
        stack = [(root, 1)]
        
        while stack:
            (curr, depth) = stack.pop()
            
            # if leaf, update the max depth
            if curr.left == None and curr.right == None:
                max_depth = max(max_depth, depth)
            
            for c in [curr.left, curr.right]:
                if c:
                    stack.append((c, depth+1))
                    
        return max_depth
                
        
        
        
#[3, 9, 20, n, n]
root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))

sol = Solution()
print(sol.maxDepth(root))