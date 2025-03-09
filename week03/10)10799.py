# https://www.acmicpc.net/problem/10799


import sys

s = sys.stdin.readline().strip()  # 입력받은 쇠막대기 및 레이저 표현 문자열
stack = []  # 스택 선언
result = 0  # 총 잘린 조각 개수 저장

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')  # 여는 괄호는 스택에 저장
    else:
        stack.pop()  # 닫는 괄호가 나오면 스택에서 제거
        if s[i - 1] == '(':
            result += len(stack)  # 레이저일 경우, 스택 크기만큼 추가 (잘린 막대 개수)
        else:
            result += 1  # 막대기의 끝일 경우, 조각 1개 추가

print(result)  # 최종 결과 출력
