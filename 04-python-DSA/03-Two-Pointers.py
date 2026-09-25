'''
# two pointer question- type 1: opposite ends
# Two pointers where you start from each end and move index left / right 
# use when you have a sorted array and need to find pair / target

nums = [0, 1, 2, 5, 6, 7, 8, 9, 15]


def two_sum_sorted(nums, target):
    left = 0 # index of left number
    right = len(nums) - 1 # get index of right number using length of the array, becasue index starts at 0 you need to do -1


    while left < right:
        total = nums[left] + nums[right]
        
        if total == target:
            print("the numbers that add to ", target, " are:", nums[left], " and ", nums[right])
            return True
        
        elif total > target:
            right -= 1

        else:
            left += 1
        
    print("there are no numbers that add to ", target)
    return False

two_sum_sorted(nums, 14)



# two pointer question- type 2: Palindrome
#given a string, determine whether its a palindrome 

text = "racecar"
def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
        
    return True

print(is_palindrome(text))



# we want to remove the duplicates in a given SORTED array
# we want unique values at the beginning: [1, 1, 2, 2, 4, 5, 5] -> [1, 2, 3, 4 ,5]
#we have to modify it in place; not allowed to make a new array

nums = [1, 1, 2, 2, 3, 5, 6, 7, 7, 7, 7, 8, 9]

def remove_duplicates(nums):
    slow = 0

    for fast in range (1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return ("the number of unique elements is ", slow + 1)

print(remove_duplicates(nums))


# practice 1: Given a string, determine whether it reads the same forwards and backwards.
# this is a palindrome question

text = "racecar"
def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
print(is_palindrome(text))


# practice 2: given an array of sorted integerts, determine whether two numbers add up to a target.
nums = [1, 2, 4, 6, 8, 11]
target = 10
def two_sum_pointers(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            print(nums[left], "and", nums[right], "add up to", target)
            return True
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -=1
    return False

print(two_sum_pointers(nums))


# practice 3 - slow/fast pointers

#Given an array, remove all occurrences of 3 in-place, keeping the other elements at the beginning.

nums = [3, 1, 3, 2, 4, 3, 5]

def slow_fast(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 3:
            nums[slow] = nums[fast]
            slow +=1
    return nums[:slow]

print(slow_fast(nums))



# given a strong, determine whether its a palindrome; igfnore spaces, punctuation, and capitalisation.

text = "racecar" 

def is_palindrome_two(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if not text[left].isalnum():
            left += 1
        elif not text[right].isalnum():
            right -= 1
        elif text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    print(text, " is a palindrome")
    return True

print(is_palindrome_two(text))    

'''

# Given a sorted array of integers, remove the duplicates in-place so that each element appears only once.

nums = [1, 1, 2, 2, 3, 3, 4]

def sort_array(nums):
    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow +=1
            nums[slow] = nums[fast]
    return nums[:slow +1]

print(sort_array(nums))
        
            
