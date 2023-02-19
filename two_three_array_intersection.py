# https://leetcode.com/problems/intersection-of-two-arrays/
# https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/


import collections

# time o(min(n, m)) and space O(n+m)
def intersection(nums1, nums2):
    return list(set(nums1).intersection(set(nums2)))
    
    
# intersection between three sorted arrays
# this solution doesn't use sorted feature
# also set messes up with orders so I have to use sorted at the end
def arraysIntersection(arr1, arr2, arr3):
    return sorted(list(set(arr1).intersection(set(arr2)).intersection(set(arr3))))
    
    
# from solution, collection.counter count the elements in the list it is given
# time and space is O(n) n being sum of len of 3 lists
def arraysIntersection2(arr1, arr2, arr3):
    ans = []
    counter = collections.Counter(arr1 + arr2 + arr3) # concatenate them together
    print(counter)
    for item in counter:
        if counter[item] == 3:
            ans.append(item)
    return ans



# to use the sorted feature, we should use pointers and update them wisely!
# start from the begining, move the one that's smaller forward.
# this is better only space wise!
def arraysIntersection3(arr1, arr2, arr3):
    ans = []
    p1 = 0
    p2 = 0
    p3 = 0
    
    while p1<len(arr1) and p2<len(arr2) and p3<len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            ans.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        else:
            if  arr1[p1] < arr2[p2]:
                p1 += 1
                
            elif arr2[p2] < arr3[p3]:
                p2 += 1
            
            else:
                p3 += 1

    return ans

# print(intersection([4,9,5], [9,4,9,8,4]))
print(arraysIntersection2([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]))