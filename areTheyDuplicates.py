# implement a function called areThereDuplicates which accepts a variable number of arguments, and checks whether there are any duplicates among the arguments passed in.
def areThereDuplicates(*args):
    dict1 = {}
    for i in args:
        dict1[i] = dict1.get(i, 0) + 1
        if dict1[i] > 1:
            return True

    return False