'''

# string reversal:

string = "hamza"

def reverse_string(string):
    new = []
    last_char = len(string) - 1

    for i in range(len(string)):
        new.append(string[last_char])
        last_char -= 1
    return "".join(new)


# removing characters:

string = "h3a4m5z6a"

def remove_numbers(string):
    cleaned = []
    for char in string:
        if char.isdigit():
            continue
        cleaned.append(char)
    return "".join(cleaned)

#string counting

string = "banana"

def count_char(string, target):
    target_count = 0
    for char in string:
        if char == target:
            target_count += 1
        
    return target_count

# case-insensitive comparison

def same_word(word1, word2):
    lower1 = word1.lower()
    lower2 = word2.lower()
    return lower1 == lower2

# valid palindrome: combines Strings + Two Pointers

s = "racecar"

def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

# valid anagram:
# Given two strings s and t, determine whether t is an anagram of s.

s = "listen"
t = "silent"

def is_anagram(s, t):
    dict1 = {}
    dict2 = {}

    for char in s:
        dict1[char] = dict1.get(char, 0) + 1
    for char in t:
        dict2[char] = dict2.get(char, 0) + 1
    
    if dict1 == dict2:
        return True
    else:
        return False


# longest common prefix:
# Given an array of strings, find the longest prefix shared by all strings.

strings = ["flower", "flow", "flight"]

def longest_common_prefix(strings):
    longest_prefix = []

    for i in range(min(len(string) for string in strings)):
        for string in strings:
            if string[i] != strings[0][i]:
                return "".join(longest_prefix)
            longest_prefix.append(strings[0][i])
        return "".join(longest_prefix)

# length of last word:
'''


s = "Hello World"

def length_last(string):
    string_stripped = string.strip()
    i = len(string_stripped) - 1
    count = 0

    while i>=0 and string_stripped[i] != " ":
        i -=1
        count +=1
    return count

print(length_last(s))