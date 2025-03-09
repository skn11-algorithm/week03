# 오름차수 push + ex)4 = [1,2,3,4] ++++
# 내림차수 pop - ex) 3 = [1,2] -- 스택의 젤 위 숫자와 입력된 수가 같으면 pop
# 입력된 숫자가 스택에 없거나 규칙 만족 x NO

n = int(input())
count =1
stack =[]
temp = True #스택수열 만족 여부
op = [] # +,- 저장 리스트

for i in range(n):
    a = int(input())
    # a 이하 숫자까지 스택에 넣음
    while count <= a:
        stack.append(count)
        op.append('+')
        count += 1
    #num 이랑 stack 맨 위 숫자가 동일하면 제거
    if stack[-1] == a:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for i in op:
        print(i)
