# input: 명령의 수 n / n개의 명령
# output: 명령에 맞는 수 출력

from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        queue.append(command[1])
        
    elif command[0] == 'pop':
        if len(queue) != 0:
            temp = queue.popleft()
            print(temp)
        else:
            print(-1)
            
    elif command[0] == 'size':
        print(len(queue))
        
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
            
    elif command[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    
    elif command[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)