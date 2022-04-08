#given an array of integers and a number, write a function called maxSubarraySum which finds the maximum sum of a subarray with the length of the number passed to the function.
def max_subarray_sum(array, num):
    if len(array) < num:
        return None
    else:
        maxSum = 0
        for i in range(0, num):
            maxSum += array[i]
        currentSum = maxSum
        for i in range(num, len(array)):
            currentSum = currentSum - array[i - num] + array[i]
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum

def max_subarray_sum_test():
    try:
        assert(max_subarray_sum([100, 200, 300, 400], 2) == 700)
        assert(max_subarray_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39)
        assert(max_subarray_sum([-3, 4, 0, -2, 6, -1], 2) == 5)
        assert(max_subarray_sum([3,-2, 7, -4, 1, -1, 4, -2, 1], 2) == 5)
        assert(max_subarray_sum([2, 3], 3) == None)
        print("Test Passed")
    except:
        print("Test Failed")

max_subarray_sum_test()