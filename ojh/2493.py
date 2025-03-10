import sys
input=sys.stdin.readline
n=int(input())
tops=list(map(int,input().rstrip().split())) # 각 탑의 높이
stack=[] # 탑의 인덱스 저장
result=[0]*n

for i in range(n):
    # 현재 탑보다 낮은 탑들은 수신할 가능성이 없으므로 제거
    while stack and tops[stack[-1]]<tops[i]:
        stack.pop() 
        
    if stack:
        result[i]=stack[-1]+1 #배열은 0부터 시작. 탑 순서는 1부터 시작하므로 +1
    
    # 현재 탑의 인덱스를 스택에 저장 (다음 탑들이 이 탑을 참고할 수 있도록)
    stack.append(i) 
    
print(*result)
