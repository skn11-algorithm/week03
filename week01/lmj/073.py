# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

n = int(input())
n -= 1 # 먼저 n을 감소시켜줌(n-1 출력을 위해)

while n >= 0: # n이 0이상일때까지 출력력
    print(n)
    n = n-1