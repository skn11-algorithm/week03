w,h,b = input().split()

result = int(w) * int(h) * int(b) / 1024 / 1024 / 8

print('%.2f'%result,"MB")