# import sys
# # 1. 입력 받기
# # 2. 입력 소스가 (나 )인지 확인하기
# # 3. 입력이 )부터 시작인지 확인
# # 4. (와 )의 갯수가 같은지 확인 -- 실패
# # 4-1 bag에 받고, pop으로 빼기
# # 4-2 빈 리스트에서 pop 사용 불가 

# arr = []
# bag = []
# # count_l = 0
# # count_r = 0
# count = 0
# a = input()
# for i in a:
#      arr.append(i)

# # print(arr)
# if arr[0] == ')':
#     print('NO')
#     # break
#     sys.exit()


# for i in arr :
#     if i != '('and i != ')' :
#         print('NO')
#         sys.exit()
#     if i == '(':
#         bag.append(i)
#     if i == ')':
#         if len(bag) == 0:
#             bag.append('a')
#             break 
#         else:
#             bag.pop()
    
# if len(bag) == 0:
#     print('YES')
#     sys.exit()
# else:
#     print('NO')
#     sys.exit()

#         # if i == '(':
#         #     count_r += 1
#         # if i == ')':
#         #     count_l += 1
#         # ())(() 의 경우 YES가 나오게 됨


#     # # No 표시후에도 돌아서 답이 두번 나옴: while True 추가-실패
#     # if count_r == count_l:
#     #         print('YES')
#     #         sys.exit()
#     # else:
#     #         print('NO')
#     #         sys.exit()

# https://kangddong.tistory.com/entry/백준-9012번-괄호-파이썬 참고...

n = int(input())

for _ in range(n):
    line = input()
    stack = []

    for i in line:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')