# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

month = int(input())
if month in (12,1,2):
    print('winter')
elif month in (3,4,5):
    print('spring')
elif month in (6,7,8):
    print('summer')
elif month in (9,10,11):
    print('fall')