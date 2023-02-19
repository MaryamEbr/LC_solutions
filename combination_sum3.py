# https://leetcode.com/problems/combination-sum-iii/
from itertools import combinations

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        comb_list = combinations(nums, k)
        for comb in list(comb_list):
            if sum(comb)==n:
                res.append(list(comb))
        
        return res
sol = Solution()
print(sol.combinationSum3(3, 9))