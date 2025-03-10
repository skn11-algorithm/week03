import sys

n = int(sys.stdin.readline())
str = list(sys.stdin.readline().strip()) # strip(): 문자열 내 공백을 모두 제거
numbers = [int(sys.stdin.readline()) for i in range(n)]

stack = []

for i,s in enumerate(str):
    if 'A' <= s <= 'Z':
        stack.append(numbers[ord(s)-ord('A')])
    else: 
        str2 = stack.pop()
        str1 = stack.pop()
        
        if s=='+':
            stack.append(str1+str2)
        elif s=='-':
            stack.append(str1-str2)
        elif s=='*':
            stack.append(str1*str2)
        elif s=='/':
            stack.append(str1/str2)
        
print('%.2f' %stack[0])
