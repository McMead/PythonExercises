#write a function called minSubarrayLen which accepts two parameters an array of positive integers and a positive integer. 
# The function should return the minimal length of a contiguous subarray of which the sum is greater than or equal to the integer passed to the function.
#  If there isn't one, return 0 instead.

def min_subarray_len(nums, sum):
    total = 0
    start = 0 
    end = 0 
    min_len = float("inf")
    
    while start < len(nums):
        if total < sum and end < len(nums):
            total += nums[end]
            end += 1 
        elif total >= sum:
            min_len = min(min_len, end - start)
            total -= nums[start]
            start += 1 
        else:
            break
    if min_len == float("inf"):
        return 0 
    else:       
        return min_len

def min_subarray_len_test():
    try:
        assert(min_subarray_len([2, 3, 1, 2, 4, 3], 7) == 2)
        assert(min_subarray_len([2, 1, 6, 5, 4], 9) == 2)
        assert(min_subarray_len([3, 1, 7, 11, 2, 9, 8, 21, 62, 33, 19], 52) == 1)
        assert(min_subarray_len([1, 4, 16, 22, 5, 7, 8, 9, 10], 39) == 3)
        assert(min_subarray_len([1, 4, 16, 22, 5, 7, 8, 9, 10], 55) == 5)
        assert(min_subarray_len([4, 3, 3, 8, 1, 2, 3], 11) == 2)
        assert(min_subarray_len([1, 4, 16, 22, 5, 7, 8, 9, 10], 95) == 0)
        print("Test Passed")
    except:
        print("Test Failed")

min_subarray_len_test()