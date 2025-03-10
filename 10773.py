# 1. 입력 받기
lst = []
sum = 0
k = int(input())

while k != 0:  
    num = input()
    num = int(num)
    if num != 0:
        lst.append(num)      
    else:   
        lst.pop()
    k = k - 1

    
# 2. 리스트에 숫자 넣기
# 3. 0이 들어오면 .pop
# 4. 리스트 내 합 리턴
for i in lst:
    sum += i

print(sum)