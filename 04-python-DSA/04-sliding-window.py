'''
# sliding window pattern:
# use when you see consecutive elements, longest/shortest substring, max number of k elements

#unlike two pointers, you are thinking of a range of elements between two boundaries, instead of individual values.

nums = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    left = 0
    right = k-1
    for slides in range(len(nums)-k):
        window_sum = window_sum - nums[left] + nums[right + 1]
        if window_sum > max_sum:
            max_sum = window_sum
        left += 1
        right += 1
    return max_sum

print("the max sum is", max_sum(nums, k))
'''


# variable size window sliding window question: the first type above was a fixed window size, next the window size isnt fixed.
#the key recognition is: looking for the longest substring, sub arraysatisfying a condition. shortes/ minimum...
#looking for "until a condition is violated"
#atleast / at most/ no more han.

#the window expands and contracts

text = "abcabcbb"

def var_slide_window(text):
    seen = set()
    left =0
    longest_length = 0
    for right in range(len(text)):
        while text[right] in seen:
            seen.remove(text[left])
            left +=1
        seen.add(text[right])

        window_length = right - left + 1
        if window_length>longest_length:
            longest_length = window_length
        
    return longest_length

print(var_slide_window(text))




