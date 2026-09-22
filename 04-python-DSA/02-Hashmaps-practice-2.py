# return True if any number appears more than once, otherwise return False.
'''
nums = [4, 7, 2, 9, 7, 3]

def contains_duplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate(nums))


# practice using dictionary
s = "banana"
def count_character(s):
    count_dictionary = {}
    for char in s:
        count_dictionary[char] = count_dictionary.get(char, 0) + 1
    return count_dictionary

print(count_character(s))


#Given a list of integers, return the first number that appears twice.
nums = [4, 7, 2, 7, 9, 4]

def appears_twice(nums):
    appears = set()
    for num in nums:
        if num in appears:
            return num
        appears.add(num)
    return None

print(appears_twice(nums))


# practice using enumerate:

nums = [5, 8, 12, 20]

#write loop using enumerate() whihc prints the numbers and their index
for index, num in enumerate(nums):
    print(index, num)


# next prqactice using enumerate with dictionaries

nums = [4, 7, 11, 15]

index_dict = {}
for index, num in enumerate(nums):
    index_dict[num] = index
print(index_dict)


#dictionary + enumerate
# create a dictionary with the indexes of each number in this array:

nums = [10, 20, 30, 40]
empty_dict = {}
for index, num in enumerate(nums):
    empty_dict[num] = index
print(empty_dict)


#two sum; return indexes of the two numbers that add to give the target

nums = [2, 7, 11, 15]
target = 9

seen = {}
for index, num in enumerate(nums):
    compliment = target - num
    if compliment in seen:
        return [seen[compliment], index]
    seen[num] = index


# Given a list of integers and a target, return True if any two different numbers add up to the target. Otherwise return False.
nums = [3, 8, 4, 6]
target = 10
seen = set()
def practice_func(nums):
    for num in nums:
        compliment = target - num
        if compliment in seen:
            return True
        seen.add(num)
    return False
print(practice_func(nums))

# Given a string, return True if any character appears more than once. Otherwise return False.

def char_repeat(text):
    seen = set()
    for char in text:
        if char in seen:
            return True
        seen.add(char)
    return False

print(char_repeat("hamza"))

'''

def first_unique(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in text:    
        if char_counts[char] == 1:
            return char
    return False

print(first_unique("aabbcd"))

