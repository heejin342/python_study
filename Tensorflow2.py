# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oXazYKVtaXiYG5BO6n96YRoAlJstQ9zx
"""

"""
MSE = 1/2n * 시그마(일에서 엔까지)(^Yi - yi)(^Yi - yi)  -> 평균제곱오차
앞 y가 예측값
뒤 y가 실제값. 정답

가설 y = Wx + b
기울기W == 가중치

1. 가설, 학습 데이터를 가지고 선형함수 형태로 표현
2. 손실함수 정의. 평균제곱오차를 이용하여 계속 갱신한다.최소비용을 만드는 과정
3. 가장 적절한 최적화된 기울기를 결정한다. 경사하강법을 적용한다.

[실습예제]
단순선형회귀(x==독립변수)가 하나인경우
학습시간 1시간 -> 10점
	 2시간 -> 20점
	 3시간 -> ?점
"""

X = [1,2,4,5]   # 훈련데이터 , 독립변수
Y = [10,20,40,50] # 종속변수 , 정답 , 기울기(가중치) 와 절편(편향)을 이용해 예츨선을 긋는다.

W = tf.Variable(tf.random_normal([1]))   #정구분포만드는 함수
b = tf.Variable(tf.random_normal([1]))


"""
1.가설정의
"""

hypothesis = W*X + b   #이게 예측값y

"""
2.비용함수정의
"""

cost_function = tf.reduce_mean(tf.square( hypothesis - Y ))


"""
3. 최적화정의
"""

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost_function)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
  sess.run(train)
  if step % 200 == 0 :
    print(step, "번 학습 결과")
    print("기존 값에 대한 예측값:" , sess.run(hypothesis),    ", 오차크기:",sess.run(cost_function) , ", 가중치(W):",sess.run(W) ,", b값:",sess.run(b), "\n")
    print("\n")

"""
독립변수가 여러개일때 . 다중 선형 회귀 실습

-->

중간고사 평가를 3번 실시해서 평점을 계산하는 사례
독립변수 x1,x2,x3 세개 
종속뱐수 y        한개

[훈련데이터] -> x_data = [[73.,80.,75.], [93.,88.,93.],[89.,91.,90.],[96.,98.,100.],[73.,66.,70.]]
y_data = [[152.],[185.],[180.],[196.],[142.]]
"""

import tensorflow as tf

x_data = [[73.,80.,75.], [93.,88.,93.],[89.,91.,90.],[96.,98.,100.],[73.,66.,70.]]
y_data = [[152.],[185.],[180.],[196.],[142.]]


X= tf.placeholder(tf.float32, shape=[None,3]) # 독립변수의 훈련데이터가 3개 들어올거임. 나중에 집어넣겠다.
Y= tf.placeholder(tf.float32, shape=[None,1])

W = tf.Variable(tf.random_normal([3,1]) , name = 'weight')   #랜덤확률을 만들어서 W에 대입. 3개의 데이터가 들어와서 정답은 1개만 만들겠다
b = tf.Variable(tf.random_normal([1]), name = 'bias')       #이렇게 값이 변경되양하는것들은 베리어블로 만든다.

# 1. 가설설정
hypothesis = tf.matmul(X,W) + b

#2. 비용함수 
cost_function = tf.reduce_mean(tf.square( hypothesis - Y ))


#3. 최적화함수
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost_function)

sess = tf.Session()
sess.run(tf.global_variables_initializer())


for step in range(5001):
  cost_val, hy_val , _ = sess.run([cost_function, hypothesis , train ] , feed_dict = {X: x_data , Y: y_data})   
  #트레인변수는 리턴값이 없을 수도있기떄문에 자리수만 맞춰주는 _ 을 사용해줬다.

  if step % 100 == 0 :
    print(step, "Cost:" , cost_val , "\nPrediction:\n" , hy_val )

#적용단계 시작 ~! 위에까지는 전부 학습단계
print("Your score will be " , sess.run(hypothesis, feed_dict={X: [[100., 70., 95.]]}))

"""
지수함수 그래프 그리기
"""
import numpy as np
import matplotlib.pyplot as plt

def exponential(lst):
  result = []
  for x in lst:
    y=np.exp(-x)
    result.append(y)
  return result
x= np.arange(-10.0,10.0,0.1)
y= exponential(x)

plt.plot(x,y)
plt.show()

"""
시그모이드 함수 그리기.
f(x)  =  1 / 1+e(-x승)
*중요*
"""

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(lst):
  result =[]
  for x in lst:
    y = 1/(1+np.exp(-x))
    result.append(y)
  return result

x = np.arange(-20.0, 20.0, 0.1)
y = sigmoid(x)

plt.plot(x,y)
plt.show()