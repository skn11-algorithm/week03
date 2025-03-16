''''
<스택수열>
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
이를 계산하는 프로그램을 작성하라.
'''
count = 1
result = []

n = int(input())  # 입력할 수열의 개수
for _ in range(n): 
    num = int(input())  # 입력될 숫자들
    stack = []  # 스택 초기화

    # 입력될 숫자가 더 클 때, 스택에 숫자를 쌓기
    while count <= num:  
        stack.append(count)  # 입력 숫자만큼 스택에 쌓는다
        result.append('+') 
        count += 1

    # 만약 스택의 가장 마지막 값이 num과 동일하다면 pop
    if stack[-1] == num:  
        stack.pop()
        result.append('-')
    else:
        # 스택 수열을 만들 수 없는 경우
        print('NO')
        break

# 결과 출력
print('\n'.join(result))
