# 탑은 왼->오 / 레이저 송신기는 왼쪽 방향으로 발사 pop
# 가장 먼저 만나는 단 한개에서만 수신 가능

#왼쪽에 자기보다 높이가 크거나 같은 가장 가까운 곳에 송신 가능, 인덱스 출력
# 수신하는 탑 없으면 0
#인덱스 1부터 시작
import sys
read_input = sys.stdin.readline  # input 대신 read_input 사용

N = int(read_input())  # 탑 개수
T = list(map(int, read_input().split()))  # 탑 높이 
stack = []
stack.append([1, T[0]])  # [인덱스, 높이] 형식으로 수정
ans = [0]  # 첫 탑은 아무것도 없으므로 0을 시작으로 하는 리스트

for i in range(1, N):
    while stack:
        if stack[-1][1] >= T[i]:  # 가장 마지막에 있는 탑이 현재 탑보다 크거나 같으면
            ans.append(stack[-1][0])  # 현재 탑은 해당 탑에서 신호를 받음
            stack.append([i + 1, T[i]])  # 현재 탑을 스택에 추가
            break
        else:
            stack.pop()  # 이전 탑이 현재 탑보다 작다면 제거
    if not stack:  # 스택이 비면
        ans.append(0)  # 0 추가
        stack.append([i + 1, T[i]])  # 현재 탑을 스택에 추가

print(*ans, end=' ')
