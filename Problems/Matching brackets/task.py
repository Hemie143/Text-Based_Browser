# put your python code here
import sys
from collections import deque

sentence = input()
stack = deque()
for i in sentence:
    if i == "(":
        stack.append('(')
    if i == ")":
        try:
            stack.pop()
        except IndexError:
            print("ERROR")
            sys.exit()


if len(stack) == 0:
    print("OK")
else:
    print("ERROR")
