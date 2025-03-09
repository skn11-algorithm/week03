# 스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
# 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 
# (LIFO, Last in First out) 특성을 가지고 있다.

# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

import sys

n = int(sys.stdin.readline().strip())  # 수열의 길이 입력
sequence = [int(sys.stdin.readline().strip()) for _ in range(n)]  # 만들고자 하는 수열 입력

stack = []  # 스택 선언
result = []  # 연산 기록 (+, -)
current = 1  # 스택에 넣을 숫자 (1부터 시작)
possible = True  # 수열을 만들 수 있는지 여부

for num in sequence:
    while current <= num:  # 현재 숫자까지 push 수행
        stack.append(current)
        result.append('+')  # push 기록
        current += 1

    if stack[-1] == num:  # 스택의 top이 목표 숫자와 같다면 pop 수행
        stack.pop()
        result.append('-')  # pop 기록
    else:  # 만들 수 없는 경우 (순서를 지킬 수 없음)
        possible = False
        break

# 결과 출력
if possible:
    print("\n".join(result))  # 연산 결과 출력
else:
    print("NO")  # 수열을 만들 수 없는 경우

