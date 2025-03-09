# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. 
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
# 그러한 수가 없는 경우에 오큰수는 -1이다.

# 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. 
# A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
result = [-1] * n  # 결과 리스트 (-1로 초기화)
stack = []  # 인덱스를 저장할 스택

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:  # 스택의 top보다 현재 값이 크면
        result[stack.pop()] = arr[i]  # 오큰수 갱신
    stack.append(i)  # 현재 인덱스를 스택에 저장

print(" ".join(map(str, result)))
