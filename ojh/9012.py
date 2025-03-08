import sys

input=sys.stdin.readline
n=int(input())
for _ in range(n):
    stack=[]
    str=(input().rstrip())
    for s in str:
        if s=='(': # 여는 괄호일 경우 스택에 넣는다
            stack.append(s)
        else : # 닫는 괄호일 때
            if stack: # 스택이 비어있지 않는 경우 
                stack.pop() 
            else: # pop할 원소가 없는 경우 NO
                print("NO")
                break
    else: # for문 다 돌고
        if not stack: # 스택이 비어있으면 온전한 수식!
            print('YES')
        else: # 비어있지 않으면 NO
            print('NO')