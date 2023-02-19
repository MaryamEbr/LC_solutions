# https://leetcode.com/problems/majority-element/
import math
import collections

class Solution(object):
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major_number = math.floor(len(nums)/2)
        di = {}

        # O(n) time and space
        for item in nums:
            if item in di:
                di[item] += 1

            else:
                di[item] = 1

            if di[item] > major_number:
                    return item



    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


        
sol = Solution()
sol.majorityElement([2,2,1,1,1,2,2])