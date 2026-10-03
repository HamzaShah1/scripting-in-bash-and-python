#You are given a list of strings representing events from a system, write a function that returns the number of "ERROR" events.

events = [
    "INFO",
    "ERROR",
    "INFO",
    "WARNING",
    "ERROR",
    "ERROR",
    "INFO"
]

def count_errors(events):
    error_nums = 0

    for word in events:
        if word == "ERROR":
            error_nums +=1
    return error_nums



# Given a list of integers, return the first number that appears twice.

nums = [4, 2, 7, 3, 2, 9, 7]

def appears_twice(nums):
    is_seen = set()
    for num in nums:
        if num in is_seen:
            return num
        is_seen.add(num)
    return -1


# Given a string, return the first character that appears only once.

s = "aabbcdde"

def appears_once(s):
    counts = {}

    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    for char in s:
        if counts[char] == 1:
            return char
    return -1

# Given an array of integers, return True if any two numbers add up to the target, otherwise return False.

nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            return complement, num
        seen.add(num)
    return -1

# Given a list of integers, return True if the list contains two consecutive numbers that are equal. Otherwise, return False.

nums = [1, 2, 3, 3, 5]

def consecutive_nums(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

# Given a list of integers, return the number of times the value target appears in the list.

nums = [1, 4, 2, 4, 5, 4, 3]
target = 4

def num_times(nums, target):
    count = 0

    for num in nums:
        if num == target:
            count += 1
    return count

# Given a list of integers, return the smallest number in the list.

nums = [7, 3, 9, 2, 5]

def smallest_num(nums):
    smallest = nums[0]

    for num in nums:
        if num < smallest:
            smallest = num
    return smallest

# Given a string, return True if it is a palindrome, and False otherwise.

s = "racecar"

def is_palindrome(string):
    left =0
    right = len(string) -1

    while left < right:
        if string[left] == string[right]:
            left +=1
            right -=1
        else:
            return False
    return True

# Given a string containing only the characters: ( ) [ ] { } return True if the brackets are properly matched and nested, otherwise return False.

def valid_brackets(s):
    