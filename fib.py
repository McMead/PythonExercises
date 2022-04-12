#write a recursive function called fib which accepts a number and returns the nth number in the fibonacci sequence.
#recall that the fibonacci sequence is the sequence of whole numbers 1, 1, 2, 3, 5, 8, ... which starts with 1 and 1,
#  and where every number thereafter is equal to the sum of the previous two numbers.

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)

def fib_test():
    try:
        assert(fib(0) == 0)
        assert(fib(1) == 1)
        assert(fib(2) == 1)
        assert(fib(3) == 2)
        assert(fib(4) == 3)
        assert(fib(5) == 5)
        assert(fib(6) == 8)
        assert(fib(7) == 13)
        assert(fib(8) == 21)
        assert(fib(9) == 34)
        assert(fib(10) == 55)
        assert(fib(28) == 317811)
        assert(fib(35) == 9227465)
        print("Test Passed")
    except:
        print("Test Failed")

fib_test()
