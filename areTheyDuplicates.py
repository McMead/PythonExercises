# frequency counter method
def areThereDuplicates(*args):
    dict1 = {}
    for i in args:
        dict1[i] = dict1.get(i, 0) + 1
        if dict1[i] > 1:
            return True

    return False

# multiple pointers method
def areThereDuplicates2(*args):
    args = sorted(args)
    for i in range(len(args)-1):
        if args[i] == args[i+1]:
            return True
    return False
