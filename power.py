# write a function called power which accepts a base and an exponent. The function should return the power of the base to the exponent. 
# This function should mimic the functionality of Math.pow() - do not worry about negative bases and exponents.

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

def power_test():
    try:
        assert(power(2, 0) == 1)
        assert(power(2, 2) == 4)
        assert(power(2, 4) == 16)
        assert(power(2, 8) == 256)
        assert(power(2, 10) == 1024)        
        print("Test Passed")
    except:
        print("Test Failed")

power_test()