# stacks follow LIFO - last in first out:
# a list works as a stack
'''
stack operations:

stack.append(x) - push
stack.pop() - remove top
stack[-1] - look at top without removing


# when questions require a stack: if you need to remember the most recent thing and deal with it before older things:

s = "({[]})"

def is_valid(s):
    stack = []

    matching = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        if char in "({[":
            stack.append(char)
        elif stack[-1] == matching[char]:
            stack.pop()
        else:
            return False
    return len(stack) == 0

print(is_valid(s))


# leetcode 833 - backpace string compare:

s = "ab#c"
t = "ad#c"

def backspace_compare(s, t):
    stack1 = []
    stack2 = []

    for char in s:
        if char != "#":
            stack1.append(char)
        elif stack1:
            stack1.pop()
    for char in t:
        if char != "#":
            stack2.append(char)
        elif stack2:
            stack2.pop()
    
    return stack1 == stack2
    
print(backspace_compare(s, t))

'''

s = "abbaca"

def remove_duplicates(s):
    stack = []

    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

print(remove_duplicates(s))





