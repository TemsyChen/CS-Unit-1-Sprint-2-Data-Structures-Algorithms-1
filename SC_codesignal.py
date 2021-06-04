'''
Two words are blanagrams if they are anagrams 
but exactly one letter has been substituted for another.
'''

'''
Understand:
"tangram", "anagram" --> true
"tangram", "pangram" --> true
'aba', 'bab' --> true
'silent', 'listen' --> false

Plan: Sort letters of words first. If all but one match, return true. 
'''

def checkBlanagrams(word1, word2):
    new_word = word1 + word2
    letters = {}
    for char in new_word:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    print(letters)
    count_dict = {"even": 0, "odd": 0}
    for char, count in letters.items():
        if count % 2 == 0:
            count_dict["even"] += 1
        elif count % 2 != 0:
            count_dict["odd"] += 1
    print(count_dict)
    return count_dict["odd"] == 2


'''
You are given a sorted array in ascending order 
that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] 
might become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's 
index. If the target value is not present in the array, return -1.
'''
'''
Understand:
nums = [4,5,6,7,0,1,2], target = 0 --> 4
nums = [4,5,6,7,0,1,2], target = 3 --> -1

Plan:

'''

def findValueSortedShiftedArray(nums, target):
    min_, pivot, max_ = 0, nums.index(max(nums)), len(nums) - 1
    result = None
    while result == None:
        if nums[max_] == target:
            result = max_
        elif nums[max_] < target:
            new_nums = nums[min_:pivot]
            result = searchHelper(new_nums, target, pivot)
        else:
            new_nums = nums[pivot:max_]
            result = searchHelper(new_nums, target, pivot)
    return result
    
def searchHelper(new_nums, target, pivot):
    min_, max_ = 0, len(new_nums) - 1
    while min_ <= max_:
        mid = (min_ + max_) // 2
        if new_nums[mid] == target:
            return mid + pivot
        elif new_nums[mid] > target:
            max_ = mid - 1
        elif new_nums[mid] < target:
            min_ = mid + 1
    return -1
 