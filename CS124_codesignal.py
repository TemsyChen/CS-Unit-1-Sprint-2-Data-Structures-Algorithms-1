'''
For a given positive integer n determine if it 
can be represented as a sum of two Fibonacci numbers (possibly equal).

Understand: 
1 --> true
11 --> true
60 --> true
66 --> false

Plan: Make a list of fibonacci numbers up to n.
 Iterate through the list to see if one value 
 plus another can equal n.

Runtime: O(n^2)
Space: O(n)
'''
    
def make_fib_list(n):
    fib_list = [0, 1]
    first_val, second_val = 0, 1
    last_val = 0
    while last_val <= n:
        last_val = first_val + second_val
        fib_list.append(last_val)
        first_val = second_val
        second_val = last_val
    return fib_list

def fibonacciSimpleSum2(n):
    fib_list = make_fib_list(n)
    print(fib_list)
    for i in fib_list[0:(len(fib_list)-1)]:
        for j in fib_list[(i+1):(len(fib_list)-1)]:
            if (i+j) == n:
                return True
    return False

'''
Given a sorted (in ascending order) integer array 
nums of n elements and a target value, write a function 
to search for target in nums. If target exists, 
then return its index, otherwise, return -1.

Understand:
nums = [-1,0,3,5,9,12], target = 9 --> 4
nums = [-1,0,3,5,9,12], target = 2 --> -1

Plan:
Use a binary search: Check the value of the middle index, 
if the target is higher than the value, reset the new 
minimum of the set to be the middle index plus one. 
If the target is lower than the value, reset the new 
maximum of the set to be the middle minus one. 
Check the value of the new middle. Use a while loop 
until the target's index is found, or if never found, return -1.

Runtime: O(log n)
Space: O(1)
'''

def csBinarySearch(nums, target):
    min_, max_ = 0, len(nums)-1
    while min_ <= max_:
        mid = (min_ + max_) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            min_ = mid + 1
        else:
            max_ = mid - 1
    return -1

#Author's Answer
def csBinarySearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1

'''
Given an integer array nums sorted in 
ascending order, and an integer target.

Suppose that nums is rotated at some pivot 
unknown to you beforehand (i.e., [1,2,3,4,5,6,7] 
might become [4,5,6,7,1,2,3]).

You should search for target in nums and if 
found return its index, otherwise return -1.

Understand:
nums = [6,7,1,2,3,4,5], target = 1 --> 2
nums = [6,7,1,2,3,4,5], target = 3 --> 4
nums = [1], target = 2 --> -1

Plan: Find the min() value in the array. Check if the target is the last value in the array. If it is greater, check the values between index 0 and the max() value index. If the target is lower than the last value, do a binary search between min index and last value.

Runtime: O(log n)
Space: O(1)
'''

def csSearchRotatedSortedArray(nums, target):
    min_, pivot_min, max_ = 0, nums.index(min(nums)), len(nums)-1
    result = None
    while result == None:
        if nums[max_] == target:
            result = max_
        elif nums[max_] < target:
            new_nums = nums[min_:pivot_min]
            result = searchHelper(new_nums, target)
        else:
            new_nums = nums[pivot_min:(max_)]
            result = searchHelper(new_nums, target)
    return result
            
def searchHelper(new_nums, target):
    min_, max_ = 0, len(new_nums) - 1
    while min_ <= max_:
        mid = (min_ + max_) // 2
        if new_nums[mid] == target:
            return mid
        elif new_nums[mid] < target:
            min_ = mid + 1
        else:
            max_ = mid - 1
    return -1

#Author's Answer
def csSearchRotatedSortedArray(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[start]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target <= nums[end] and target > nums[mid]: 
                start = mid + 1
            else:
                end = mid - 1
    return -1
