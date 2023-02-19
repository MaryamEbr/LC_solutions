# Definition for a binary tree node.
            
            

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    
    #not mine, copied from solution
    # it's dfs recursive
    # O(n), each node is seen once
    # NOK, space depend on how many time we call the recursive function
    # if tree is one line, we call it n times so space is O(n)
    # if tree is balanced, we call it logn times so space is O(log n)
    def minDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        print(root.val)
        min_depth = 0
        
        # if empty
        if not root:
            return 0
        
        
                
        children = [root.left, root.right]
        # if we're at leaf node
        if not any(children):
            return 1
        
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1 
        
        
    # dfs with help of iteration and a stack, not recursive
    # with a little bit of help from solution (the idea of keeping depth in the stack)
    def minDepth(self, root):
        min_depth = float('inf')
        stack = [(root, 1)]
        
        if not root:
            return 0
        

        while stack:
            (curr, depth) = stack.pop()
            # print(curr.val, [(a.val, i) for (a, i) in stack])
            
            # if leaf, update the min_depth
            if curr.left == None and curr.right == None:
                min_depth = min(depth, min_depth)
                
            # else, continue traversing
            for c in [curr.left, curr.right]:
                if c:
                    stack.append((c, depth+1))

        return min_depth    



# [2, n, 3, n, 4, n, 5, n, 6]
# root = TreeNode(2, left=None, right=\
#                 TreeNode(3, left=None, right=\
#                          TreeNode(4, left=None, right=\
#                              TreeNode(5, left=None, right=\
#                                  TreeNode(6, left=None, right=None)))))


#[3, 9, 20, n, n]
root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))

sol = Solution()
print(sol.minDepth(root))