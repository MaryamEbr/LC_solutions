# https://leetcode.com/problems/combination-sum/
from itertools import combinations, product



class Solution(object):
    
    ### correct but time limit exceed
    def combinationSum1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        until = int(target/min(candidates))

        for i in range(1,until+1):
            comb_list = product(candidates, repeat=i)
            for comb in list(comb_list):
                if sum(comb)==target:
                    
                    if self.check(comb, res) == False:
                        res.append(comb)
                    

        return [list(a) for a in res]     
    
    def check (self, el, arr):
        for a in arr:
            if sorted(a) == sorted(el):
                return True
        return False
                
    # trying to use backtracking
    def combinationSum(self, candidates, target):
        
        
        
        
    
    
                
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))
print(sol.combinationSum([2,3,5], 8))