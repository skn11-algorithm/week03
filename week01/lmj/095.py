# 오랜만에 집에 간 영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 생각해 보다가
# "바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다.

# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

d=[] #1. 우선 d라는 빈 리스트에 작은 리스트19개를 만들고, 0을 채워넣는다.
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0) 

n = int(input()) #2. 흰 돌을 놓을 갯수를 n으로 입력하고 
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1 # 3. 흰 돌을 놓을 좌표를 배열로 입력 

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')
  print()
