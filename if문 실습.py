"""
파이썬 자료형 실습 예제
1.리스트 - [] ,
2.튜플 - () ,
3.dictionary - {}
이 세 가지가 중요하다
"""
int_data = 10               #정수 선언
float_data = 3.14           # 실수 선언
str_data1 = "안뇽 나는 희진이야"      #문자형 변수 선언
str_data2 = "Hi, Im heejin"          

list_data = [10,20,30,40,50]
tuple_data = (10,20,30)
dict_data = {'name' : '손흥민' , 'age':28}

print(int_data)
print(float_data)
print(str_data1)
print(str_data2)
print(list_data)
print(tuple_data)
print(dict_data)



#if문 실습
scope = [10,20,30,40,50]

x=10
y=20

if x>y:
    print('x 가 y 보다 크거나 같습니다')

elif x<y:
    print('x 가 y 보다 작습니다')
    
else:
    print('x와 y가 같습니다')


for x in range(1,4):
    print(x)

for x in scope:
    print(x)
    
for x in scope:
    print(x, end=' ')

print('\n')

for x in scope:
    print(x)
    if(x<30):
        continue
    else:
        break

for x in scope:
    print(x)
else:
    print("perpect")


#연산자 실습
a=10/2
print(a)      #실수로 출력된다.

b=10 //2
print(b)      #정수로 출력 된다 



#시퀀스 자료형
#문자열 리스트 튜플은 순서를 가진 자료형이지만, dict은 key가 있기 때문에 순서가 필요없다.

str_data = 'abcd'
list_data = [10,[20,30],'파이썬']
tuple_data = (100,200,300)  #값 변경이 불가능하다.



#문자열의 끝은 음수(-1)인덱스로 표현한다.
#[7]부터 [13]이 끝이면([13] == [-1]), 슬라이싱 할때 [7:] 이렇게 해주면 됨
#거꾸로 해서 [-1:-7] 해줘도 된다
"""
[m:n]인덱스가 m이상 n 미만인 요소를 슬라이싱
[:n]처음부터n 미만인 요소를 슬라이싱
[m:]m 부터 끝까지
[:-n]처음부터 끝에서 n번째 미만인 요소를 슬라이싱!!
[-m:]끝에서 m 번째 이상인 모든 요소
[:]처음부터 끝까지
[::2]2칸단위로 슬라이싱
[::-1]역으로 슬라이싱,거꾸로 배열할때 씀!!

"""

str_data = 'Time is money!!'   #문자열 객체 생성
print(str_data[1:5])         #ime 출력
print(str_data[:7])          #Time is 출력
print(str_data[9:])         #oney!!
print(str_data[:-3])        #Time is mone
print(str_data[-3:])        #y!!
print(str_data[:])           #Time is money!!
print(str_data[::-1])
print(str_data[::2])
















