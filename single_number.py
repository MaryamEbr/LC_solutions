# https://leetcode.com/problems/single-number/



# O(n log n + n), with sorting
# space is O(1)
def singleNumber(nums):
    nums = sorted(nums)
    
    i = 0
    while(i<len(nums)-1):
        if nums[i] != nums[i+1]:
            return nums[i]
        i += 2
    if len(nums)==1 or nums[-1] != nums[-2]:
        return nums[-1]
        
        
        
# with dictionary, hash table
# time and space O(n)
def singleNumber2(nums):

    di = {}
    for n in nums:
        if n in di:
            di[n] += 1
        else:
            di[n] = 1
            
    for key in di:
        if di[key] == 1:
            return key

# this has a xor solution with constant space that I don't really get it
# https://leetcode.com/problems/single-number/solutions/127660/single-number/
def singleNumber3(nums):
    a = 0
    for i in nums:
        a ^= i
    return a


print(singleNumber2([4,1,2,1,2]))
# print(singleNumber2([1]))
            