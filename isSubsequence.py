#Write a function called isSubsequence which takes in two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. 
# In other words, the function should check whether the characters in the first string appear somewhere in the second string, without their order changing.
def is_subsequence(str1, str2):
    i = 0
    j = 0
    
    while j < len(str2):
        if str2[j] == str1[i]:
            i += 1
        if i == len(str1):
            return True
        j += 1
        
    return False
    
def is_subsequence_test():
    try:
        assert(is_subsequence("hello", "hello world") == True)
        assert(is_subsequence("sing", "sting") == True)
        assert(is_subsequence("abc", "abracadabra") == True)
        assert(is_subsequence("abc", "acb") == False)
        print("Test Passed")
    except:
        print("Test Failed")

is_subsequence_test()