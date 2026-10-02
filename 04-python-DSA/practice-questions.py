#multiple choice questions
'''
1. set - we only need to see if it already exists in the set or not
2. this is a binary search - we are repeatedly eliminating half of the search space
3. C - pop, popleft() is for queues
4. A - for i in range(len(nums)) - this loops through the entire array of nums with each num at value i
5. checking if its a palindrome; use two pointers, one on each end: right and left: so answer is B
6. B - task is "A" and tasks contains ["B", "C"], a queue is FIFO - first in first out, popleft() removes A
7. C - if we are talking about a path, but the max depth is 2
8. nums.sort() creates a new array
9. A - use a set to lkeep track of which characters are currently present - i forgot how to do this leetcode problem though
10. return True because theyre both the same
'''

# in an array, see if any value appears more than once:
nums = [4, 7, 2, 7, 9, 4]

def is_seen(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# find two values whos sum equals target and return their indices
nums = [2, 7, 11, 15]
target = 9
# we want to find the 'compliment' of the target - ie: number - what = target, and if it already exisst in the dictionary then we have the number; so return its index

def two_sum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        
        seen[num] = index

# find first value that appears twice as you scan left to right:
nums = [3, 1, 3, 5, 2]

def is_seen(num):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

# determine how many times each value appears
nums = [2, 4, 2, 7, 4, 2]

def count_freq(nums):
    dict = {}

    for num in nums:
        dict[num] = dict.get(num, 0) + 1
    return dict

#whether list contains two values whose sum equals 6: nums = [1, 2, 3, 4, 5]

nums = [1, 2, 3, 4, 5]
target = 6

def equal_six():
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [nums[left], nums[right]]
        
        elif total < target:
            left += 1
        else:
            right -=1
    
    print( nums[left], "and ", nums[right], " equal ", target)





