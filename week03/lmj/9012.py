#1. 틀렸습니다
T = int(input()) # 몇 개의 기호 줄을 받을지 입력 (정수형)

for _ in range(T): # 의미없는 변수 (T번의 코드가 돌아가는 동안)
    a = input() # 입력받을 문자열 
    stack = [] # 입력될 stack을 초기화 

    # 문자열 처리 블럭
    for i in a:
        if i == '(':
            stack.append(i) # 입력될 값이 (라면  스택에 추가
        elif i == ')': # 입력될 값이 ) 라면 :
            if len(stack) == 0: # stack의 길이를 확인한 후, 
                print('NO')
                break
            else: # (를 pop 해서 쌍을 맞춰준다!!
                stack.pop()

    # 남아있는 문자열 (쌍이 안맞는 것 판별) 처리 블럭 
    # 모든 문자를 처리한 후. 스택에 남아있는 괄호가 있다면  No!!
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')



#2. 런타임 에러
T = int(input()) 
for _ in range(T): 
    a = input()
    stack = []  

    for i in a:
        if i == '(':
            stack.append(i) 
        elif i == ')': 
            if len(stack) != 0: 
                stack.pop()
            else: 
                print('No')
                break

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')




#3. 구글링 ㅜ
t = int(input())

for _ in range(t):
    stack = []
    a = input()
    check = True
    for i in a:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                check = False
                break
            if stack[-1] != '(':
                check = False
                break
            else: # 스택이 비어있지 않고 ( 값이 들어 있다면 ( 값 빼서 다시 비워 줘
                stack.pop()
    if check and not stack: # 입력받은 ps 값 전부 검증하고 나온 후 체크 값이 트루고 스택이 비어있지 않을 때
        print('YES')
    else:
        print('NO')