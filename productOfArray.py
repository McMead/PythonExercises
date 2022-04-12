# write a function called productOfArray which takes in an array of numbers and returns the product of them all.
# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])

def product_of_array(arr):
    if not arr:
        return 1
    return arr.pop() * product_of_array(arr)

def product_of_array_test():
    try:
        assert(product_of_array([1, 2, 3, 4]) == 24)
        assert(product_of_array([1, 2, 3, 4, 5]) == 120)
        assert(product_of_array([1,2,3]) == 6)
        assert(product_of_array([1,2,3,10]) == 60)
        assert(product_of_array([]) == 1)
        assert(product_of_array([1]) == 1)
        print("Test Passed")
    except:
        print("Test Failed")

product_of_array_test()