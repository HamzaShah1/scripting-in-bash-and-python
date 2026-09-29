# array traversal:
#if we want to return the largest num and index:

'''
nums = [4, 7, 2, 9, 1]

def largest(nums):
    largest_num = nums[0]
    largest_index = 0
    for i in range(len(nums)):
        if nums[i] > largest_num:
            largest_num = nums[i]
            largest_index = i
    return largest_num, largest_index

print(largest(nums))



#array count:
nums = [2, 4, 2, 7, 2, 9]
target = 2

def count_target(nums, target):
    count = 0

    for i in range(len(nums)):
        if nums[i] == target:
            count += 1
    
    return count

print(count_target(nums, target))

'''

nums = [8, 3, 6, 1, 9, 4]

def find_min(nums):
    min = nums[0]
    min_index = 0
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
            min_index = i
    return min, min_index

print(find_min(nums))

#building a result array:

nums = [1, 2, 3, 4]

def double_array(nums):
    result = []
    for num in nums:
        result.append(num*2)
    return result

#filtering an array:

nums = [1, 4, 7, 2, 9, 6]

def even_nums(nums):
    evens = []
    for num in nums:
        if num % 2 ==0:
            evens.append(num)
    return evens


# in place operation:

nums = [1, 2, 3, 4, 5]

def in_place():
    for i in range(len(nums)):
        nums[i] = (nums[i])*2
    return nums

# searching and returning an index
nums = [4, 8, 2, 9, 5]
target = 9

def find_target():
    index = 0
    for num in nums:
        if num == target:
            return index
        else:
            index +=1
    return -1
        
# arrays exercise: Write a function that returns how many times 7 appears.

nums = [3, 7, 2, 7, 9, 7]

def seven_count():
    seven_count = 0
    for num in range(len(nums)):
        if nums[num] == 7:
            seven_count += 1
    return seven_count

        