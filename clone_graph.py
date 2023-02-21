# https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        # wrong, unsolved
        
        # edge case
        if node == None:
            return None
        
        if node.neighbors == []:
            return Node(node.val)
        
        visited = set()
        queue_old = [node]
        queue_new = [Node(node.val)]
        
        
        while queue_old:
            curr_old = queue_old.pop(0)
            curr_new = queue_new.pop(0)
            
            for neigh in curr_old.neighbors:
                neigh_new = Node(neigh.val)
                curr_new.neighbors.append(neigh_new)
                
                if neigh not in visited:
                    visited.add(neigh)
                    queue_old.append(neigh)
                    queue_new.append(neigh_new)
                    
                    
        
        