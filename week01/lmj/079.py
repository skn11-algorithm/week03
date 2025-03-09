n = int(input())

sum = 0
total = 0

while sum < n : # 총합이 입력값보다 작을때까지
  total += 1
  sum += total
  
print(total)
