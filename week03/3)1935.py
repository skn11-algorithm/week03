# 후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

# 후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.


import sys

N = int(sys.stdin.readline().strip())  # 피연산자 개수
expression = sys.stdin.readline().strip()  # 후위 표기식
values = [int(sys.stdin.readline().strip()) for _ in range(N)]  # 피연산자 값

operands = {}
for i in range(N):
    operands[chr(ord('A') + i)] = values[i]  # A~Z와 값 매칭

stack = []

for char in expression:
    if char.isalpha():  # 피연산자 (A~Z)
        stack.append(operands[char])  # 값 넣기
    else: 
        b = stack.pop()
        a = stack.pop()
        
        if char == '+':
            stack.append(a + b)
        elif char == '-':
            stack.append(a - b)
        elif char == '*':
            stack.append(a * b)
        elif char == '/':
            stack.append(a / b) 

# 4. 결과 출력 (소수점 둘째 자리까지)
print(f"{stack[-1]:.2f}")
