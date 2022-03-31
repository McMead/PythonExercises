#write a function called average_pair. 
# Given a list of integers and a target average, determine if there is a pair of values in the list where the average of the pair equals the target average.
#  There may be more than one pair that matches the average target.
def average_pair(sortedArray, target):
    first = 0
    second = 1
    for i in range(0, len(sortedArray)):
        calculated_average = int((sortedArray[first] + sortedArray[second]) / 2)
        if calculated_average == target:
            return True
        else:
           first = first + 1
           second = second + 1
            
    return False
    



def average_pair_test():
    try:
        #([1,2,3], 2.5) == True
        average_pair([1,3,3,5,6,7,10,12,19], 8) == True
        #average_pair([-1,0,3,4,5,6], 4.1) == False
        average_pair([],4) == False
        print("Test Passed")
    except:
        print("Test Failed")
        
average_pair_test() 