"""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are the same. 

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""

def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]