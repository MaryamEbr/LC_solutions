# https://leetcode.com/problems/contains-duplicate/
# https://leetcode.com/problems/contains-duplicate-ii/description/


# kinda brute force
# first sort and the a loop
# O(n log n + n)
def containsDuplicate(nums):
    
    nums = sorted(nums)
    for i in range(len(nums)-1):
        if (nums[i] == nums[i+1]):
            return True
    return False


# using python dictionary
# little faster, but more space
def containsDuplicate2(nums):
    
    di = {}
    for i, num in enumerate(nums):
        if num not in di:
            di[num] = i
        else:
            return True
    return False


# from user solution
# nice one line python using sets

def containsDuplicate3(nums):
    return True if len(set(nums)) < len(nums) else False




# another similar problem, contains duplicate with distance k
# time ans space O(n)
def containsNearbyDuplicate(nums, k):
    
    di = {}
    for i, num in enumerate(nums):
        if num not in di:
            di[num] = i
        elif  num in di and abs(di[num]-i)>k:
            di[num] = i
        elif num in di and abs(di[num]-i)<=k:
            return True
    return False

# print(containsDuplicate3([1,2,3, 4]))
print(containsNearbyDuplicate([1,0,1,1], 1))
