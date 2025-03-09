# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
# 첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.
import datetime
days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

x, y = map(int,input().split())
day = days[datetime.date(2007,x,y).weekday()]
print(day)