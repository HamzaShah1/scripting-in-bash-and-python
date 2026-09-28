'''
# Given a sorted array of integers nums and an integer target, return the index of target if it exists. Otherwise, return -1.

nums = [1, 3, 5, 7, 9, 11]
target = 7

def binary_search(nums, target):
    left=0
    right=len(nums)-1

    while left <= right:
        midpoint = (left+right)//2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] > target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

print(binary_search(nums, target))


# Given a sorted array of integers nums that may contain duplicates, return the first index at which target appears. If target does not exist, return -1.

nums = [1, 2, 2, 2, 4, 5, 6]
target = 2

def first_appearance(nums, target):
    left = 0
    right = len(nums)
    answer = -1

    while left <= right:
        midpoint = (left+right)//2

        if nums[midpoint] == target:
            answer = midpoint
            right = midpoint - 1
        elif nums[midpoint] < target:
            left = midpoint+1
        else:
            right = midpoint - 1
    return answer

print(first_appearance(nums, target))

'''

# Given a sorted array of integers, return the index of the first number greater than or equal to target.

nums = [1, 3, 5, 7, 9]
target = 6

def boundary_binary(nums, target):
    left=0
    right=len(nums) - 1
    answer = -1

    while left <= right:
        midpoint = (left+right)//2

        if nums[midpoint] >= target:
            answer = midpoint
            right = midpoint - 1
        elif nums[midpoint]<target:
            left = midpoint + 1
    return answer

print(boundary_binary(nums, target))

