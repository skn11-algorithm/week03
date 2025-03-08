import sys
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().rstrip().split()))
result=[-1]*n
stack=[]
# 오른쪽에서 왼쪽으로 탐색
for i in range(n-1,-1,-1):
    # 스택의 top이 나보다 작으면 오큰수가 아니므로 제거
    while stack and nums[i]>=stack[-1]:
        stack.pop()

    # 스택이 비지 않으면 오큰수가 있음
    if stack:
        result[i]=stack[-1]

    stack.append(nums[i])
print(*result)