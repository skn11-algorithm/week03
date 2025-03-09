# 정수 k 주어짐
k = int(input())
# 저장할 스택 필요요
stack = []

for _ in range(k):
    n = int(input())# 정수가 한개씩 주어짐
    if n == 0:
        stack.pop() 
    else:
        stack.append(n) #정수 저장
        
a = sum(stack)
print(a)



