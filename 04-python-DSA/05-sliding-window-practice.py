
# fixed size sliding window

'''
nums = [1, 12, -5, -6, 50, 3]
k = 4

def max_average(nums, k):
    left=0
    right=k-1
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for slides in range(len(nums)-k):
        window_sum = window_sum - nums[left] + nums[right+1]
        if window_sum > max_sum:
            max_sum = window_sum
        
        left+=1
        right+=1
    max_average = max_sum/k

    return max_average

print(max_average(nums, 4))



# variable size sliding window:
# Given a string text, find the length of the longest substring containing only unique characters.

text = "dvdf"

def sliding_window_var(text):
    seen = set()
    left=0
    longest_length=0

    for right in range(len(text)):
        while text[right] in seen:
            seen.remove(text[left])
            left+=1
        seen.add(text[right])
        
        window_length = right - left + 1
        if window_length > longest_length:
            longest_length = window_length
    return longest_length

print(sliding_window_var(text))

'''

# practice 3 - frequency / count sliding window 
# Given a string text, find the length of the longest substring containing at most 2 distinct characters.

text = "ccaabbb"

def freq_count_slide(text):
    counts = {}
    left = 0
    longest_length=0

    for right in range(len(text)):
        counts[text[right]] = counts.get(text[right], 0) + 1

        while len(counts) > 2:
            counts[text[left]] -=1
            if counts[text[left]] == 0:
                del counts[text[left]]
            left +=1
        
        window_length = right - left + 1
        if window_length>longest_length:
            longest_length = window_length

    return longest_length

print(freq_count_slide(text))
           
