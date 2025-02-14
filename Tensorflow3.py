# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Diu0gv7XSbpm5_86v-X9meyN2P2ivd7m
"""

"""
지도학습
 -->분류
1. 바이너리 클래시키케이션(이항)의 분류 -> 정답이 둘중에 하나
2. 멀티노미얼 클래시피케이션(다항)의 분류
 -> A , B ,C
시그모이드 ->활성함수

<바이너리 클래시피케이션 실습>

"""
import tensorflow as tf

#훈련데이터 독립변수 x , 종속변수 y
x_data = [[1,2],[2,3],[3,1],[4,3],[5,3],[6,2]] #앞에께 x1 = 공부한시간 , 위에꺼 x2 = 인강본시간
y_data = [[0],[0],[0],[1],[1],[1]]


X = tf.placeholder(tf.float32 , shape = [None, 2])
Y = tf.placeholder(tf.float32 , shape = [None, 1])

W =tf.Variable(tf.random_normal([2,1]), name = 'weight')   #2개가 입렫되어서 1개가 나올거임
b =tf.Variable(tf.random_normal([1]), name = 'bias')      

#학습모델

hypothesis = tf.sigmoid(tf.matmul(X,W) + b)   # 활성화 함수 적용
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1-Y)*tf.log(1-hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

activation_func =tf.cast(hypothesis > 0.5, dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(activation_func, Y), dtype=tf.float32))

sess= tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(10001):
  cost_val, _ = sess.run([cost, train], feed_dict={X:x_data, Y:y_data})
  if step % 2000 == 0:
    print("%05d" %step, cost_val)
h,c,a = sess.run([hypothesis , activation_func , accuracy], feed_dict={X:x_data, Y:y_data})

print("\n[10000번 학습결과]")
print("1. 시그모이드 적용: " , h.T)
print("2. 활성화 함수 적용결과",[int(x) for x in c])
print("3. 기존 정답과 비교", sum(y_data, [])) #빈 리스트를 주면 하나로 합치라는얘기임
print("4. 정확도 (Accuraty)" , a)

#위에까지는 학습단계 . 이제부터 적용단계
print("\n공부한 시간 2시간 / 학습 동영상 본 시간 2시간 일때, 합격 여부는?" , sess.run(hypothesis, feed_dict={X:[[2,2]]}))
print("\n공부한 시간 5시간 / 학습 동영상 본 시간 2시간 일때, 합격 여부는?" , sess.run(hypothesis, feed_dict={X:[[5,2]]}))

"""
로그함수 실습 -> 로그함수의 특징

불연속인것을 해결하기 위해서 압축이 필요한데, 이때 필요한데 로그함수이다.
y가 0에 가까울수록 -무한개에 가까워지고, 1에 가까울수록 0에 가까워진다.

"""
import tensorflow as tf

node1 = tf.constant(0.00001, tf.float32)   #저기 0을 넣으면 무한대로 간다
log_value = tf.log(node1)

sess= tf.Session()
print(sess.run(log_value))

"""
Multinommial classification 실습예제
"""
import tensorflow as tf

x_data =[[1,2,1,1],[2,1,3,2],[3,1,3,4],[4,1,5,5],[1,7,5,5],[1,2,5,6],[1,6,6,6],[1,7,7,7]]
y_data = [[0,0,1],[0,0,1],[0,0,1],[0,1,0],[0,1,0],[1,0,0],[1,0,0],[1,0,0]]     #순서대로 c학점, b학점, a학점

X= tf.placeholder("float", [None,4])
Y= tf.placeholder("float", [None,3])

W = tf.Variable(tf.random_normal([4,3]), name = 'weight')
b = tf.Variable(tf.random_normal([3]), name = 'bias')

#학습모델 만들기

hypothesis = tf.nn.softmax(tf.matmul(X,W)+b)   #softmax 가 합을 1로 만들어버린다
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1)) #1을주면 행단위로, 0이면 열단위로 sum을 내는거거임

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

#그래프 Launch

with tf.Session() as sess: #앞으로 세션안에서 그래프를 동작시키겠다
  sess.run(tf.global_variables_initializer())

  for step in range(3001):
    sess.run(optimizer, feed_dict={X:x_data, Y:y_data})
    if step % 200 == 0:
      print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}))

#적용단계
  a=sess.run(hypothesis, feed_dict={X:[[1,11,7,9]]})
  print(a, sess.run(tf.argmax(a,1)))

