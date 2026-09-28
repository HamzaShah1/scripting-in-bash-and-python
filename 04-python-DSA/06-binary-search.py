#classic binary search
# find a target in a sorted array

'''        
nums = [2, 5, 8, 12, 16, 23, 38, 45, 56]
target = 23

def binary_search(nums, target):
    
    left = 0
    right = len(nums) - 1 

    while left <= right:
        midpoint = (left+right) // 2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1
    
    return -1

print(binary_search(nums, 16))
'''        
#binary search practice:

nums = [3, 7, 11, 18, 24, 31, 42, 50]
target = 31

def binary_search(nums, target):

    left = 0
    right = len(nums) -1

    while left <= right:
        midpoint = (right + left) // 2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] > target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

print(binary_search(nums, target))
