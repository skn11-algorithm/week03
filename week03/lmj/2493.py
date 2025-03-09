#####구글링....
# 
# ---> 결국 왼쪽 방향으로 자기보다 높은 탑에서 수신을 받는 것!!!!
# 
# 
num = int(input())
lst = list(map(int, input().split()))
stack = []
result = [0]*num # 입력받을 배열들을 일단 0으로 초기화 

for i in range(num):
    if stack: # 스택이 비어있지 않다면, 즉 왼쪽에 탑이 존재한다면
        while True: # 탑들과 비교하면서 
            if lst[i] <= stack[-1][0]: # 현재 숫자가 스택의 마지막값보다 작거나 같다면,
                result[i] = stack[-1][1] + 1 # 위치를 결과 배열에 저장하고 
                stack.append([lst[i], i]) # 스택에 추가함 
                break
            else: # 현재 탑보다 낮은 탑 
                stack.pop() 
            if not stack: # 스택이 비어있는 경우 현재 숫자를 추가하고 break 
                stack.append([lst[i], i])
                break
    else: # 왼쪽에 탑이 존재하지 않는다면!!!!
        stack.append([lst[i], i])

print(*result) # 파이썬 언패킹 : 리스트 내부 요소들이 공백으로 구분되어 출력 