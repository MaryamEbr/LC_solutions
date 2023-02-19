# leetcode 15
# https://leetcode.com/problems/3sum/description/


# brute force O(n^3)
# time limit exceeded
def three_sum(nums):
    
    result = []
    
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i]+nums[j]+nums[k] == 0 and i!=j and j!=k:
                    if set([nums[i],nums[j],nums[k]]) not in [set(a) for a in result]:
                        result.append([nums[i],nums[j],nums[k]])
    
    return result

# i guess O(n^2)
# still time limit exceeds
def three_sum2 (nums):
    result = []
    nums_dict = {}
    for i, num in enumerate(nums):
        nums_dict[num] = i
        
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if 0-(nums[i]+nums[j]) in nums_dict and nums_dict[0-(nums[i]+nums[j])]!=i and nums_dict[0-(nums[i]+nums[j])]!=j:
                if set([nums[i],nums[j],0-(nums[i]+nums[j])]) not in [set(a) for a in result]:
                    result.append([nums[i],nums[j], 0-(nums[i]+nums[j])])

    return result



# let's sort it first
# I guess O(n^3)
# time limit exceeded
def three_sum3 (nums):
    # O(n log n)
    nums = sorted(nums)
    result = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] > 0:
                break
            
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] > 0:
                    break

                if nums[i]+nums[j]+nums[k] == 0:
                    
                    if set([nums[i],nums[j],nums[k]]) not in [set(a) for a in result]:
                        result.append([nums[i],nums[j],nums[k]])
                    
    return result

# based on leetcode solution
# time limit exceed
def three_sum4 (nums):
    nums = sorted(nums)
    result = []
    
    for i in range(len(nums)-2):
        if nums[i]>0:
            break

        low = i+1
        high = len(nums)-1
        
        while high>low:
            if nums[i] + nums[low]+ nums[high] == 0:

                if set([nums[i],nums[low],nums[high]]) not in [set(a) for a in result]:
                    result.append([nums[i],nums[low],nums[high]])
                    
                high -= 1
                low += 1 
            
            if nums[i] + nums[low]+ nums[high] > 0:
                high -= 1
                
            if nums[i] + nums[low]+ nums[high] < 0:
                low += 1        
    return result




# based on leetcode solution
# more help from dolution
# O(n log n (sort) + n^2)

def three_sum5 (nums):
    nums = sorted(nums)
    result = []
    
    for i in range(len(nums)-2):
        if nums[i]>0:
            break

        low = i+1
        high = len(nums)-1
        
        if i == 0 or nums[i - 1] != nums[i]:
            while high>low:
                
                if nums[i] + nums[low]+ nums[high] > 0:
                    high -= 1
                    
                elif nums[i] + nums[low]+ nums[high] < 0:
                    low += 1    
                
                else:
                    result.append([nums[i],nums[low],nums[high]])
                        
                    high -= 1
                    low += 1 
                
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                        
    
    return result

print(three_sum5([-1,0,1,2,-1,-4]))