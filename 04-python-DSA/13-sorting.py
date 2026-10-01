# difference between sorted() and .sort()
# sorted() makes a new list
#.sort() charngesd the original list
'''
nums = [8, 3, 1, 7, 4, 2]
print(nums.sort())

#BUBBLE SORT:

nums = [5, 2, 4, 1]

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

print(bubble_sort(nums))

# selection sort

def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

# insertion sort

def insertion_sort():
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1

        while j>=0 and nums[j] > current:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = current

    return nums


# sorting coding practice:

# bubble sort

nums = [5, 2, 8, 1, 3]

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# selection sort

def selection_sort(nums):
    for i in range(len(nums)):
        smallest_index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[smallest_index]:
                smallest_index = j
        nums[i], nums[smallest_index] = nums[smallest_index], nums[i]
    return nums

# insertion sort
# do some practice coding insertion sort

'''
# merge intervals - leetcode

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

intervals = [[1,3], [2,6], [8,10], [15,18]]

def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]


    for i in range(1, len(intervals)):
        current = intervals[i]

        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)

    return merged



