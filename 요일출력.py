"""

현재 시스템의 년월일요일 localtime

"""

from time import localtime

##요일 이름을 리스트 객체로 생성한다.
weekdays = ['월', '화', '수' , '목' , '금' , '토' , '일']

t=localtime()


#time 이라는 구조체에서 요일을 가지고오면 요일은 숫자로 제시해준다. -> 0:월요

today= '%d-%d-%d' %(t.tm_year , t.tm_mon, t.tm_mday)     #출력 형식 포매팅


#추가
day = weekdays[t.tm_wday]

print('[%s' %(today))
print('-%s요일]' %(day))

print('[%s-%s요일]' %(today,day))
     