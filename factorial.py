#write a function factorial which accepts a number and returns the factorial of that number. 
# A factorial is the product of an integer and all the integers below it; e.g., factorial four (4!) is equal to 24, because 4 * 3 * 2 * 1 equals 24.
# factorial zero (0!) is always 1.
def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1 
    return num * factorial(num - 1)
    
def factorial_test():
    try:
        assert(factorial(1) == 1)
        assert(factorial(2) == 2)
        assert(factorial(4) == 24)
        assert(factorial(7) == 5040)
        print("Test Passed")
    except:
        print("Test Failed")
        
factorial_test()