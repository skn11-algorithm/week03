# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = map(int,input().split()) # 두 값 한꺼번에 형변환하기
print(bool(a) and bool (b))