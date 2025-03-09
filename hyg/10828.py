# input: 명령의 수 n / n줄에 걸쳐 명령이 하나씩 주어짐
# output: 명령에 맞는 수 출력

import sys

stack = []

n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) != 0:
            temp = stack.pop()
            print(temp)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
        