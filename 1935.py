# 후위 표기법 =  연산자를 만나면 두개의 피연산자를 꺼내 계산 후 다시 스택에 넣는 방식

#입력 개수
N =int(input())

#후위 표기법 문자열로 입력
T = input()

# N개의 숫자를 저장할 리스트를 초기화
num_list = [0]*N #길이가 N 이고 모든 값이 0인 리스트트

#스택
stack =[]

for i in range(N):
    num_list[i] = int(input()) #num_list 에 숫자 저장

for i in T: #T 한글자씩 확인하면서 계산 수행
    if 'A' <= i <= 'Z': # A~Z 범위 안 문자 들어올 시 num_list 에서 가져옴
        stack.append(num_list[ord(i)-ord('A')]) #ord = 문자 열을 아스키 코드로 반환 할 수 있는 함수
    #A 부터 시작하는 인덱스를 0 부터 맞추기 위해 ord A 를 뺴준다
    else:
        str2 = stack.pop() # pop() 시 스택의 마지막 값이 나옴
        str1 = stack.pop()

        if i == '+':
            stack.append(str1 + str2)  
        elif i == '-':
            stack.append(str1-str2)
        elif i == '*':
            stack.append(str1*str2)
        elif i == '/':
            stack.append(str1/str2)


print('%.2f'%stack[0])

#chr() = 아스키코드를 문자열로 변환하는 함수