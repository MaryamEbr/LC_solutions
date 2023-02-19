# https://leetcode.com/problems/missing-number/




# time and space O(n)
def missingNumber(nums):
    
    nums_set = set(nums)
    full_set = set(range(0, len(nums)+1))
    return list(full_set-nums_set)[0]


# use that bit manipulation thingy to reduce the space to O(n)
# nope
# there's some xor thingy I don't feel like thinking about
def missingNumber2(nums):
    
    for num_ind in nums:
        if num_ind == len(nums):
            continue
        
        if nums[abs(num_ind)] >=0 :
            nums[num_ind] *= -1
            
        else:
            pass
        
        

# this was kinda smart
# using a closed-form expression for the sum until n (n(n+1)/2)
# it's probably just for this problem, time O(n) and space O(1)
def missingNumber3(nums):
    n = len(nums)
    sum_nums = n*(n+1)/2
    return int(sum_nums-sum(nums))
    
print(missingNumber3([9,6,4,2,3,5,7,0,1]))