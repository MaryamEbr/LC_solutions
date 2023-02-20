# https://leetcode.com/problems/combination-sum/
from itertools import combinations, product

# the backtrack algorithm
# Backtrack(x)
#     if x is not a solution
#         return false
#     if x is a new solution
#         add to list of solutions
#     backtrack(expand x) probably with a loop

class Solution(object):
    
    ### correct but time limit exceed
    # brute force, O(n!) i guess!! time limit exceed
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
    # from solution not mine
    def combinationSum(self, candidates, target):
        
        result = []
        
        # the recursive function
        def backtrack(remain, combination, start):
            
            # if we reached target, add to result and return
            #### NOK!!! this should be deep copied, 
            # other wise we change combination and it will change here too
            if remain == 0:
                result.append(list(combination))
                return        
            
            # if we exceed the target, return
            if remain < 0:
                return
            
            # expand the combination
            for i, num in enumerate(candidates[start:]):
                combination.append(num)
                backtrack(remain-num, combination, i+start)
                ## pop becase we're backtracking
                combination.pop()
            
            
        backtrack(target, [], 0)
        return result
        
        
        
        
        
    
    
                
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))
print(sol.combinationSum([2,3,5], 8))