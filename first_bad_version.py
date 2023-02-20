# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version<=4:
        return False
    else:
        return True

class Solution(object):

    # binary search becase the array is sorted
    # wrong
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        while start <= end:
            
            mid = (start+end)//2

            if isBadVersion(mid) and (mid==1 or  not isBadVersion(mid-1)):
                return mid

            elif not isBadVersion(mid):
                start = mid+1

            else:
                end = mid-1
                
        return -1


    # non binary version, O(n), linear, 
    # time issue
    def firstBadVersion1(self, n):
        for i in range(n):
            if isBadVersion(i+1):
                return i+1


sol = Solution()
print(sol.firstBadVersion(5))