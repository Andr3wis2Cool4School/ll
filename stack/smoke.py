# First in Last Out 
# FILO

# this is a stack 
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

# [1, 2, 3]

# pop the stack value
temp = stack.pop()
print(temp)

while len(stack) > 0:
    temp = stack.pop()
    print(temp)
