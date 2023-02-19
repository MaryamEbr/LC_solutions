# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/



# time and space O(n)
def findDisappearedNumbers(nums):
    n = len(nums)
    nums_set = set(nums)
    full_set = set(range(1, n+1))
    return list(full_set-nums_set)
    
    
    
# print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))