======STRINGS=========

length
len(text)

slicing
text[0:5]

iteration
for char in text:
    print(char)

useful methods:
text.lower() - lowercase
text.upper() - uppercase
text.strip() - removes whitespace from start or end
text.split() - returns a list where text between specified seperator becomes list items
text.replace() - replaces a string with another string

char.isdigit() - checks if a character is a number or not

"".join(["list", "of", "items"]) - join lists together with no space, do " " to join with a space. also the ites youre joining need to be strings

.get() - get a value of a key in a dictionary and give a default value if it doesnt exist already


enumerate() 
you use enumerate when you want both the index and the value while looping through a list


stack operations:

stack.append(x) - push
stack.pop() - remove top
stack[-1] - look at top without removing

