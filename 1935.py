# 1. 문자열 리스트로 받기
# 2. 기호랑 알파벳 분리 << 실패
# 3. 각 숫자 대입하기
# 4. 식에 나중에 대입하는 것이 아닌, 순서대로 계산

# k = int(input())
# lst = input()
# lst_t = list[lst]
# nums = []
# while k != 0:
#     nums.append(int(input()))
#     k - 1

# for i in nums:

# https://animoto1.tistory.com/entry/백준-1935-후위-표기식2-파이썬-Python 참고
# 1935 후위 표기식2
n = int(input())
word = input()                # 후위표기식을 word에 저장함
num_lst = [0]*n				  # 피연산자값을 저장하기 위한 num_lst 생성	

for i in range(n):
    num_lst[i] = int(input())  # 피연산자값 받기

stack = []                    # stack 리스트를 통해 후위표기식 계산

for i in word :					
    if 'A' <= i <= 'Z' :		# 후위표기식에서 알파벳을 만나면 stack에 저장한다.(물론 알파벳 형태가 아닌 피연산자값의 형태로)
        stack.append(num_lst[ord(i)-ord('A')])
    else :						# 연산자를 만나면
        str2 = stack.pop()		# stack 리스트의 마지막 2항목을 꺼내와서 계산한다.
        str1 = stack.pop()

        if i =='+' :
            stack.append(str1+str2)
        elif i == '-' :
            stack.append(str1-str2)
        elif i == '*' :
            stack.append(str1*str2)
        elif i == '/' :
            stack.append(str1/str2)

print('%.2f' %stack[0])			# '%.2f' % 함수를 통해 소수점 자릿수를 제한한다.