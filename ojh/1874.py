import sys

input=sys.stdin.readline
n=int(input())
nums=[int(input()) for _ in range(n)]

count=1 # push 할 숫자
stack=[] # 스택
result=[] # +, - 저장

for num in nums:
    # 1. count 변수를 이용해 1부터 오름차순으로 숫자를 push
    while count<=num: # 2-1. num이 나오기 전까지 push 연산을 수행
        stack.append(count)
        result.append("+")
        count+=1
    if stack and stack[-1]==num: # 2-2. num이 top에 도달하면 pop을 실행
        result.append("-")
        stack.pop()
    else: # 2. 만약 stack[-1]이 num과 다르면 해당 수열을 만들 수 없으므로 "NO"를 출력하고 프로그램을 종료
        print("NO")
        exit()

# 최종 출력
print("\n".join(result))
        