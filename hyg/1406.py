import sys

str = list(input())
n = int(input())
cursor = len(str)

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'L' and cursor > 0:
        cursor -= 1
    elif command[0] == 'D' and cursor < len(str):
        cursor += 1
    elif command[0] == 'B' and cursor > 0:
        str.pop(cursor-1)
        cursor -= 1
    elif command[0] == 'P':
        str.insert(cursor, command[1])
        cursor += 1

for i in range(len(str)):
    print(str[i], end='')