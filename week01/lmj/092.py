# 정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

# 선생님은 출석부를 보고 번호를 부르는데,
# 학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부른다.

# 그리고 얼굴과 이름이 잘 기억되지 않는 학생들은 번호를 여러 번 불러
# 이름과 얼굴을 빨리 익히려고 하는 것이다.

# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.


'''
모범답안입니다ㅜㅜ
'''
n = int(input()) # 개수를 입력받아 n에 정수 저장장
a = input().split() # 공백을 기준으로 잘라 a에 순서대로 저장장

for i in range(n) : 
  a[i] = int(a[i]) # a에 순서대로 저장되어 있는 값을 정수로 변환해 다시 저장한다다

d = []
for i in range(24) :
  d.append(0) # 빈 리스트에 24개의 정수값을 추가할 수 있음음

for i in range(n) :
  d[a[i]] += 1 # 번호를 부를 때마다 번호에 대한 카운트가 1씩 증가함함

for i in range(1, 24) :
  print(d[i], end=' ') # 총 카운트 출력