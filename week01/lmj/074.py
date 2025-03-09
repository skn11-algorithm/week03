# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

# 예시
# c = ord(input())
# t = ord('a')
# while t<=c :
#   print(chr(t), end=' ')
#   t += 1

your = ord(input()) # ord는 문자를 정수로 변환함함
f = ord('a') # 첫 문자를 a로 고정

while f <= your:
    print(chr(f), end=' ') #chr는 정수를 문자로 변환함
    f += 1