

# o(n)
def reverse1 (input):
    input=list(input)
    for i in range(int(len(input)/2)):
        temp = input[i]
        # can't assign values to string, so it should be list
        # strings are immutable (once you create a string, you cannot change its contents), unlike lists that are mutable
        input[i] = input[len(input)-1-i]
        input[len(input)-1-i] = temp
    
    return ''.join(input)

# easier, works on both strings and lists
# o(n)
def reverse2 (input):
    return input[::-1]

# cleaner, one line code
# lambda arguments : expression
reverse3 = lambda x :x[::-1]

print(reverse3('hello'))