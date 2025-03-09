# 첫번째 줄에 정수 k가 주어진다
k = int(input())
stack = []

for _ in range(k):
    a = int(input()) # 직접 입력하는 정수 
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

s = sum(stack)
print(s)