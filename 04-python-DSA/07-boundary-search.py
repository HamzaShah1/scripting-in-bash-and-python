# instead of looking for a specific value, we are looking for the first position where a condition becomes true:
 # we use midpoint again but if we find a value 

nums = [1, 1, 1, 2, 2, 2, 2, 3, 3]
target = 2

def boundary_search(nums, target):
    left = 0
    right = len(nums) - 1
    answer = - 1

    while left <= right:
        midpoint = (right+left) // 2

        if nums[midpoint] == target:
            answer = midpoint
            right = midpoint - 1
        
        elif nums[midpoint] > target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    
    return answer

print(boundary_search(nums,target))