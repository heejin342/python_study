"""

리스트 객체 이해하기

"""

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d']
list3 = [1,'a','abc',[1,2,3,4,5] , ['a','b','c','d']]
list4 = [(2018, 35000),(2019,50000)]   #리스트 안에 튜플()


list1[0]=6 #리스트는 값을 수정할 수 있다.
print(list1)
print(list4[0])
    

def myfunc():
    print('안녕하세요')
    
list5 = [1,2,myfunc]
list5[2]()   #==myfunc()


print('--------------------------------------------------')
#---------------------------------

year = 2019
month = 11
day = 5

print('%d-%d-%d' %(year, month, day))
print('오늘 날짜는 {}년 {}월 {}일 입니다.'.format(year, month , day)) 
print('오늘 날짜는 {year}년 {month}월 {day}일 입니다.'.format(year=2019, month=11,day=5)) 
#윗 방법은 키를 주는 거입. 키에대한 value의 값을 꼭 넣어줘야


print('{0:*>10}' .format('235,000'))
#왼쪽부터 별로 채워라 



print('---------------------------------------------')
#---------------------------------

listdata =[10,20,30]
tupledata = (10,20,30)
listdata[0] =50
#tupledata[0] = 50
print(listdata)
print(tupledata)


print('---------------------------------------------')
#---------------------------------

#파이썬 함수 만들기
def add(n1, n2):
    ret = n1+n2
    return ret

def add_txt(t1, t2):
    print(t1+t2)
    
ans = add(10,15)
print(ans)

text1= 'python'
text2= 'Good'
add_txt(text1, text2)



print('')




















