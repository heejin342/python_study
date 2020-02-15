"""
    append()함수의 중요성
"""
import numpy as np


#리스트 append
list_data = []
year = 2018  
total_sales = 150000000

list_data.append((year, total_sales))  #안에괄호는 튜플, 밖에 괄호는 함수괄호 , append 함수는 반드시 하나의 인자만 넣어야한다.

print(list_data)



#배열만들기
arr1= np.arange(15)
arr2= np.arange(1,10,0.5)    #10 보다 작은 0.5까지

print(arr1)
print(arr2)


#넘파이는 모든 배열의 숫자를 실수로 출력해준다ㅣ
data1 =[0.1,5,4,12,0.5]
a1 = np.array(data1)
print(a1)


#배열을만들고 dtype으로 타입을 정해줄 수 있음
ar = np.array([1,2,3], dtype=np.float)
print('int : {}'.format([1,2,3]))
print('float : {}'.format(ar))
print('dtype : {}'.format(ar.dtype))



#Numpy 활용하여 행렬의 곱을 연산하기
A=np.array([[1,2,3],[4,5,6]])
B=np.array([[-1,-2],[-3,-4],[-5,-6]])

C= np.dot(A,B)
print(A)
print(B)
print(C)



C1= A@B
print(C1)


"""
넘파이 패키지를 활용한 전치행렬 계산하기

"""

AA1 = np.array([[1,2],[3,4],[5,6]])
AA = np.array([[1],[2],[3],[5]])

BB = AA.T 

print(AA)
print(BB)

print("AA shape = >" ,AA.shape)
print("AA shape = >", BB.shape)