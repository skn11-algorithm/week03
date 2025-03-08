import sys
input=sys.stdin.readline
n=int(input().rstrip())
str=input().rstrip()
stack=[]
num=[]

for _ in range(n):
    num.append(int(input().rstrip()))

for s in str:
    if 'A'<=s<='Z':
        stack.append(num[ord(s) - ord('A')])
    else:
        x=stack.pop() # 두 번째 피연산자 # 순서 중요!
        y=stack.pop() # 첫 번째 피연산자
        
        if s=='*': # 계산하고 다시 push
            stack.append(y*x)
        elif s=='/':
            stack.append(y/x)  
        elif s=='+':
            stack.append(y+x)
        elif s=='-':
            stack.append(y-x)

print("%.2f"%stack.pop())