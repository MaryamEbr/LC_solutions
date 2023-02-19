# https://leetcode.com/problems/two-sum/description/
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/ (sorted version)


# brutefoce O(n^2) time O(1) space
def two_sum(nums, target):
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target and i!=j:
                return [i, j]
    

# faster
# chat gpt says O(n), but really?
def two_sum2(nums, target):
    # keys are numbers and values are indexes
    nums_dict = {} 
    for i, num in enumerate(nums):
        if target-num in nums_dict and nums_dict[target-num] != i:
            return sorted([i, nums_dict[target-num]])
        nums_dict[num] = i
        
    return []
    
    
    
# leetcode solution
# same as chat gpt solution, 
# apparently python dictionary lookup (implemented as hash map) in nearly constant time
# O(n) time
# O(n) space
def two_sum3 (nums, target):
    # build a hash table for a faster look up
    # O(n)
    nums_dict = {}
    for i, num in enumerate(nums):
        nums_dict[num] = i
        
    for i, num in enumerate(nums):
        if target-num in nums_dict and nums_dict[target-num] != i:
            return [i, nums_dict[target-num]]



# what is the array is sorted
# still time limit exceeds
def two_sum4(nums, target):
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] > target:
                break
            if nums[i]+nums[j] == target and i!=j:
                return [i, j]
            
            
# leetcode solution
# special case where the array is sorted
# O(n)

def two_sum5 (numbers, target):
    low = 0
    high = len(numbers)-1
    
    while (low<high):
        if numbers[low] + numbers[high] == target:
            return [low+1, high+1]
        
        if numbers[low] + numbers[high] > target:
            high -= 1
        
        if numbers[low] + numbers[high] < target:
            low += 1
    
print(two_sum4([0, 0, 0, 0, 0, 0, 0, 2, 3 , 9 , 9 ,9 ,9 ,9 ,9],5))