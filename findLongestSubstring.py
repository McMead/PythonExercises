#write a function called findLongestSubstring, which accepts a string and returns the length of the longest substring with all distinct characters.
def find_longest_substring(string):
    max_count = 0
    count = 0
    end = 0
    start = 0
    dict1 = {}
    for idx in range(0, len(string)):
        if string[idx] in dict1:
            max_count = max_count if max_count > count else count
            start = dict1[string[idx]]
        else:
           dict1[string[idx]] = idx
           end += 1
           count = end - start
           max_count = max_count if max_count > (end - start) else count
    
    return max_count
            
    
def find_longest_substring_test():
    try:
        assert(find_longest_substring('') == 0)
        assert(find_longest_substring('rithmschool') == 7)
        assert(find_longest_substring('thisisawesome') == 6)
        assert(find_longest_substring('thecatinthehat') == 7)
        assert(find_longest_substring('bbbbbb') == 1)
        assert(find_longest_substring('longestsubstring') == 7)
        print("Test Passed")
    except:
        print("Test Failed")
        
find_longest_substring_test()