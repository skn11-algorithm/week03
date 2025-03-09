#입력한  숫자 n 번 만큼 
# 괄호를 입력할 창이 필요요
# 괄호가 쌍으로 붙어있으면 안에 글자가 들어있어도 vps = YES
# 그 외 NO

n = int(input())

for _ in range(n):
    line = input()
    stack =[] #자료구조 열린 괄호를 만나면 스택에 추가(push), 닫힌괄호는 짝 괄호를 제거 (pop)

    for i in line:
        if i == '(':
            stack.append('(') #열린괄호는 짝을 이뤄야하니까 저장장
        elif i ==')':
            if len(stack) == 0: #닫힌 괄호 먼저 존재할 경우
                stack.append(')')
                break # 루프 종료
            else:
                stack.pop() #스택이 비어있지 않으면 ( 제거

    if len(stack) != 0: # 스택이 비어있지 않으면 no
        print('NO')
    else:
        print('YES')

