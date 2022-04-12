#write a function called recursiveRange which accepts an integer and adds up all the numbers from 0 to the number passed to the function.

def recursive_range(num):
    if num == 0:
        return 0
    return num + recursive_range(num - 1)

def recursive_range_test():
    try:
        assert(recursive_range(6) == 21)
        assert(recursive_range(10) == 55)
        assert(recursive_range(0) == 0)
        print("Test Passed")
    except:
        print("Test Failed")

recursive_range_test()
