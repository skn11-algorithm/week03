# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.

a, b = input().split()
r1 = int(a) + int(b)
r2 = int(a) - int(b)
r3 = int(a) * int(b)
r4 = int(a) // int(b)
r5 = int(a) % int(b)
r6 = int(a) / int(b)

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(format(r6,".2f"))