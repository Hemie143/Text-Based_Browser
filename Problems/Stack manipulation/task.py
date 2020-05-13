from collections import deque

n = int(input())
my_stack = deque()
for _ in range(n):
    cmd = input()
    if cmd.startswith('PUSH'):
        _, v = cmd.split(' ')
        my_stack.append(v)
    elif cmd.startswith('POP'):
        my_stack.pop()
    else:
        print("Wrong action")
while len(my_stack) > 0:
    print(my_stack.pop())
