# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque  # 큐를 위해 deque 사용

n = int(sys.stdin.readline().strip())  # 명령 개수 입력
queue = deque()  # 큐 선언

for _ in range(n):
    command = sys.stdin.readline().strip().split()  # 명령어 입력
    
    if command[0] == "push":
        queue.append(int(command[1]))  # push X: 정수 X를 큐에 삽입
    elif command[0] == "pop":
        print(queue.popleft() if queue else -1)  # pop: 큐에서 가장 앞 정수를 제거 후 출력 (없으면 -1)
    elif command[0] == "size":
        print(len(queue))  # size: 큐 크기 출력
    elif command[0] == "empty":
        print(0 if queue else 1)  # empty: 큐가 비어있으면 1, 아니면 0
    elif command[0] == "front":
        print(queue[0] if queue else -1)  # front: 큐의 맨 앞 정수 출력 (없으면 -1)
    elif command[0] == "back":
        print(queue[-1] if queue else -1)  # back: 큐의 맨 뒤 정수 출력 (없으면 -1)
