import sys
read_input = sys.stdin.readline

n = int(read_input())
a = list(map(int,read_input().split()))

stack =[]
nge = [-1]*n # 오큰수가 없는 경우 가정하기 위해 -1 로 초기화 함

for i in range(n):
    while stack and a[stack[-1]] < a[i] : # a의 가장 마지막에 있는 값과 a[i]를 비교
        # < 경우 오큰수를 찾았다는 뜻
        idx = stack.pop() # 그 값을 꺼낸다
        nge[idx] = a[i]
    stack.append(i)

print(*nge,end = ' ')
        



