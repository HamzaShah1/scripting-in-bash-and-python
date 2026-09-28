# binary search type 3: 

nums = [1, 3, 5, 6]
target = 4

def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        midpoint = (left+right)//2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return left

print(search_insert(nums, target))