# pre-reading: string manipulation

#clean strings
def clean_string(given_string):
    cleaned_string=given_string.strip().lower()
    return cleaned_string

print(clean_string(" HaMZa   "))

#count vowels
def count_vowels(text):
    vowel_count = 0
    for char in text:
        if char in "aeiou":
            vowel_count +=1
    return vowel_count

print("there are ", count_vowels("hamza"), " vowels")

#count characters
def count_characters(text):
    char_count = {}
    for char in text:
        if char not in char_count:
            char_count.update({char: 1})
        else:
            char_count[char] += 1
    return char_count

print(count_characters("hamza is cool"))

#more consise version of count characters
def count_char(text):
    char_count={}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(count_char("hamza is cool"))

# Pattern 1 - Hashmaps and Sets# if the question is asking us to remember if something has already been seen, we need to think of dictionaries or sets
#sets for unique values

# Q) Given an integer array, return TRUE if any value appears at least twice.

#we need to see if we have already seen an integer before
nums = [4,5,7,8,9,3,5,7,7,4,2]
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            print(num, "is seen already.")
            return True
        else:
            seen.add(num)
    return False

contains_duplicate(nums)

# Q) check if two strings are anagrams
def is_anagram(string1, string2):
    dict1 = {}
    dict2 = {}
    for char in string1:
        dict1[char] = dict1.get(char, 0) + 1
    for char in string2:
        dict2[char] = dict2.get(char, 0) + 1
    if dict1 == dict2:
        print(string1, " is an anagram of ", string2)
        return True
    return False

is_anagram("hamza", "haamz")

# Q) two sum - we wan to return the indexes of the two numbers in our array that add up to our target
nums = [2, 7, 11, 15]
target = 9

def two_sum():
    indexes = {}
    count=0
    for num in nums:
        indexes[num] = indexes.get(num, count)
        count += 1
         
    


