# 후위 표기식
# 후위 표기식은 연산자가 등장하면 앞의 피연산자들을 뒤부터 계산하는 방식이다.

# 첫줄 : 입력할 피연산자 개수
# 숫자인지 연산자인지 구분하여 stack에 넣어주면 됨!!!

n = int(input())
cal = input() # 후위표기식 저장 
num_lst = [0] * n # 피연산자를 받을 리스트 (저장할 리스트를 미리 확보하고 초기값 설정하는 역할)

stack = [] # 후위표기식을 계산하기 위한 스택

for i in range(n):
    num_lst[i] = int(input())

for i in cal: # a,b,c 등의 문자열을 하나씩 확인하는 반복문 
    if 'A' <= i <= 'Z':
        stack.append(num_lst[ord(i)-ord((i))])
    else: # 문자가 아닐경우 스택에서 pop해줌.
          # stack에는 문자만 
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1+str2)
        elif i == '-':
            stack.append(str1-str2)
        elif i == '*':
            stack.append(str1*str2)
        elif i == '/':
            stack.append(str1/str2)

print('%.2f' %stack[0])