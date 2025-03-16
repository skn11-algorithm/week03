# A, B, C, D, E, F 중 하나가 입력될 때,
# 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.


num = int(input(), 16)

# 1부터 num까지 곱한 16진수 구구단 출력
for i in range(1,16):
    print('%X'%num, '*%X'%i, '=%X'%(num*i), sep='')
