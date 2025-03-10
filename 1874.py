# # 1. 길이가 n인 오름차순 수열 만들기: input = 3 -> [1, 2, 3]
# # 2. 이후에 입력되는 숫자들 받기: 리스트2
# # 1->2->3->4 에서 4를 pop 한 후, 2로 돌아갈 수는 없음
# # 3. 
# # 4. 불가능할시 NO 표시

# import sys

# k = int(input())
# count = k
# lst = []
# cal = []
# lstt = []

# for i in range(1, k+1):
#     lst.append(i)

# while count != 0:
#     lstt.append(int(input()))
#     count -= 1

# # n이 lstt의 요소보다 작으면, 값이 같아질때까지 +
# # 같아졌을때 lstt 첫번째 숫자 pop, lst에서도 pop
# # 
# n = 0
# while len(lstt) != 0:
#     for _ in lst:
#         if lst[n] < lstt[0]:
#             cal.append('+')
#             n += 1
#         if lst[n] == lstt[0]:
#             del lstt[0]
#             lst.remove(lst[n])
#             cal.append('-')
#             n -= 1
#         if lst[n] > lstt[0]:           
#             if lst[n] - lstt[0] >= 2:
#                 print('NO')
#                 sys.exit()

# for i in cal:
#     print(i)

# sys.exit()

# # IndexError: list index out of range

#https://data-flower.tistory.com/98 참고
n = int(input())
stack, ans, find = [], [], True
# 숫자 1부터 시작
now = 1
for _ in range(n):
    num = int(input())
    # 스택 쌓기 Push
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    # 스택 꺼내기 Pop
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    # 불가능한 경우
    else:
        find = False

# 정답 출력
if not find: # 불가능하다면
    print('NO')
else:
    for i in ans:
        print(i)