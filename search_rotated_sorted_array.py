class Solution(object):
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target not in nums:
            return -1
        return nums.index(target)
    
    
    # with the help of solution
    # first find pivot (the min), with binary search
    # then look for target on either left sub array of right sub array (again with binary search)
    def search(self, nums, target):    
        
        # edge case
        if len(nums) == 0:
            return -1

        
        # look for pivot
        pivot_ind = -1
        start = 0
        end = len(nums)-1
        print(nums)
        
        while True:
            
            mid = (start+end)//2
            print(nums[start], nums[end], nums[mid])
            
            if mid<len(nums)-1 and nums[mid] > nums[mid+1]:
                pivot_ind = mid+1
                break
            
            elif mid>0 and nums[mid] < nums[mid-1]:
                pivot_ind = mid
                break
            
            elif mid>0 and nums[start] > nums[mid-1]:
                end = mid-1
            
            elif mid<len(nums)-1 and nums[mid+1] > nums[end]:
                start = mid+1
                
            else:
                pivot_ind = start
                break
                
    
        print("pivot_ind", pivot_ind)
        # now we have the pivot index, we have left and right sorted sub arrays
        # find the subarray that possibly contain the target
        if nums[pivot_ind] == target:
            return pivot_ind
        if pivot_ind==0 or pivot_ind==len(nums)-1:
            print("case1")
            start = 0
            end = len(nums)-1
        elif target > nums[-1]:
            print("case2")
            start = 0
            end = pivot_ind-1
        elif target <= nums[-1]:
            print("case3")
            start = pivot_ind + 1
            end = len(nums)-1
            
            
        print(start, end)
        while start<=end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid + 1
                
        return -1    
        
        
        
        
        
        
sol = Solution()
print("^", sol.search([4,5,6,7,0,1,2], 2))