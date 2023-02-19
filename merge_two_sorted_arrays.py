

# sorted's time complexity is O(n log n)
# O(m+n log m+n)
def merge_two_sorted_arrays(arr1, arr2):
    return sorted(arr1+arr2)

# faster way
# O(m+n) fastest
def merge_two_sorted_arrays2(arr1, arr2):
    result = []
    i = 0
    j = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # add what is left
    result += arr1[i:]
    result += arr2[j:]
    return result

print(merge_two_sorted_arrays2([0, 3, 4, 23, 31], [2, 4, 6, 30]))

# print(merge_two_sorted_arrays2([0, 3, 4, 23, 31], []))