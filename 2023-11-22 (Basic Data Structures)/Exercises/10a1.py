# Create an implementation of a stack using Python's built-in list type
# Be sure to implement the following methods:
# push()
# pop()
# top()
# is_empty()

stack = []


def push(item):
    stack.append(item)


def pop():
    return stack.pop()


def top():
    return stack[-1]


def is_empty():
    return len(stack) == 0


push(1)
push(2)
push(3)
print(stack)
print(pop())
print(top())
print(is_empty())
print(stack)
