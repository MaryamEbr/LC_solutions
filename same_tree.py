# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # trying a iterative approach to traverse both trees
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if not p and not q:
            return True
        
        if (p and not q) or (not p and q):
            return False

        
        stack_p = [p]
        stack_q = [q]
        
        while stack_p and stack_q:
            curr_p = stack_p.pop(0)
            curr_q = stack_q.pop(0)
            
            if curr_p.val != curr_q.val:
                return False
            
            p_neigh = [curr_p.left, curr_p.right]
            q_neigh = [curr_q.left, curr_q.right]
            
            for p_n, q_n in zip(p_neigh, q_neigh):
                if p_n and q_n:
                    if p_n.val != q_n.val:
                        return False
                    else:
                        stack_p.append(p_n)
                        stack_q.append(q_n)
                        
                if (p_n==None and q_n!=None) or (p_n!=None and q_n==None):
                    return False
        
        if (len(stack_p)==0 and len(stack_q)!=0) or (len(stack_p)!=0 and len(stack_q)==0):
            return False
    
        return True
        
    
#p = [1,2], q = [1,null,2]
# p = TreeNode(1, left=TreeNode(2))
# q = TreeNode(1, right=TreeNode(2))


# p = [1,2,3], q = [1,2,3]
# p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
# q = TreeNode(1, left=TreeNode(2), right=TreeNode(3))

# p = [1,2,1], q = [1,1,2]
p = TreeNode(1, left=TreeNode(2), right=TreeNode(1))
q = TreeNode(1, left=TreeNode(2), right=TreeNode(2))

p = None
q = None

sol = Solution()
print(sol.isSameTree(p,q))