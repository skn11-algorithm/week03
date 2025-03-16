'''답안 참조했습니다
'''


n=int(input())
for i in range(1,n):
    for j in range(n-i,0,-1): print(" ",end='')
    print("*",end='')
    for j in range((i-2)*2+1): print(" ",end='')
    if i!=1: print("*",end='')
    print()
for i in range((n-1)*2+1): print("*",end='')