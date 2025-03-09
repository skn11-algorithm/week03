# 스택에 푸시하는 순서는 오름차순을 지키도록 함
# 1234 - 123 - 12 - 125 - 1256 - 1257 - 12578 - 1257 - 125 - 12 - 1
# 43687521

import sys
input = sys.stdin.readline

n = int(input())

cursor = 1
stack = []
result = []

for i in range(n):
    num = int(input())
    
    while cursor <= num:
        stack.append(cursor)
        result.append('+')
        cursor += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        result.clear()
        result.append('NO')
        break
    
for r in result:
    print(r)

