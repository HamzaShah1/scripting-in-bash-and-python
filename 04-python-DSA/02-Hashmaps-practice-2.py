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


def first_unique(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in text:    
        if char_counts[char] == 1:
            return char
    return False

print(first_unique("aabbcd"))


# Given a list of strings, group together all strings that are anagrams of each other.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

def anagrams(list_of_strings):
    keys = {}
    for text in list_of_strings:
        key = "".join(sorted(text))
        if key in keys:
            keys[key].append(text)
        else:
            keys[key] = [text]
    return keys

print(anagrams(words))
    

# Q 1 Given a list of integers, return the first number that appears more than once.

nums = [5, 3, 8, 3, 9, 5]
seen = set()
def is_seen(nums):
    for num in nums:
        if num in seen:
            return num
        else:
            seen.add(num)
    return seen

print(is_seen(nums))

# Given a list of integers, return the number that appears most frequently.

nums = [4, 2, 4, 7, 2, 4]

def most_freq(nums):
    num_freq = {}

    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1
    
    highest_freq = 0
    highest_count = 0

    for num, freqs in num_freq.items():
        if freqs > highest_count:
            highest_count = freqs
            highest_freq = num
    return highest_freq

print(most_freq(nums))
'''

# last hashmap question

# Given a string, return the character that appears most frequently.

s = "banana"

def most_frequent_char(text):
    char_freq = {}

    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    highest_freq = 0
    highest_count = 0

    for char, freq in char_freq.items():
        if freq > highest_count:
            highest_count = freq
            highest_freq = char
    return highest_freq

print(most_frequent_char(s))

