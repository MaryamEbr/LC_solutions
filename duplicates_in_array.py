# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/



# it should be O(n) with constant space
# but this solution doesn't have constant space
def findDuplicates(nums):
    
    n = len(nums)
    di = dict(zip(range(1, n+1), [0 for a in range(n)]))
    
    for item in nums:
        di[item] += 1
        
    result = []
    for key in di:
        if di[key] == 2:
            result.append(key)
    return result

# using this key information that numbers are from 1 to len(nums)
# each element-1 is a valid index, and each element is >0

def findDuplicates2(nums):

    result = []
    for i,num_ind in enumerate(nums):
        if nums[abs(num_ind)-1] > 0:
            nums[abs(num_ind)-1] *= -1
        else:
            result.append(abs(num_ind))
            
    return result
    
# print(findDuplicates2([4,3,2,7,8,2,3,1]))
print(findDuplicates2([1]))