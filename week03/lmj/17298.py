N = int(input())
seq = list(map(int, input().split()))
stack = []
result = [-1] * N # 결과 배열을 역순으로 초기화시킨다

for i in range(N):
    while stack and seq[i] > seq[stack[-1]] : # stack이 비어있지않음 & 현재 수열이 스택의 top보다 크면 
        result[stack.pop()] = seq[i] # -> pop한 수를 현재 값으로 설정한다다
    stack.append(i) # 스택에 저장 

print(result)