# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

your = input()

if your == 'A':
    print('best!!!')
elif your == 'B':
    print('good!!')
elif your == 'C':
    print('run!')
elif your == 'D':
    print('slowly~')
else:
    print('what?')