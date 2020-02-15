# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SnxF2JpDxys35bEHzO7YqQj96by-Sl-i
"""

import numpy as np
import tensorflow as tf


x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],[1],[1],[0]]

x_data = np.array(x_data, dtype = np.float32)
y_data = np.array(y_data, dtype = np.float32)

X = tf.placeholder(tf.float32, [None,2])
Y = tf.placeholder(tf.float32, [None,1])
W = tf.Variable(tf.random_normal([2,1]) , name = 'weight')
b = tf.Variable(tf.random_normal([1]) , name = 'bias')

hypothesis = tf.sigmoid(tf.matmul(X,W) + b)
cost = -tf.reduce_mean(Y * tf.log(hypothesis)+(1-Y)*tf.log(1-hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

predicted = tf.cast(hypothesis >0.5 , dtype= tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype= tf.float32))


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(10001):
        sess.run(train, feed_dict = {X:x_data , Y:y_data})
        if step % 500 == 0 :
            print(step, sess.run(cost, feed_dict = {X:x_data , Y:y_data}), sess.run(W))
            
            h,c,a = sess.run([hypothesis, predicted , accuracy], feed_dict = {X:x_data , Y:y_data})
            print("\nHyppothesis:" , h ,"\nCost:" ,c, "\nAccuaracy:", a)

"""
XOR 문제를 딥러닝으로 해결하자
"""
import tensorflow as tf
import numpy as np

x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],[1],[1],[0]]

x_data = np.array(x_data, dtype = np.float32)
y_data = np.array(y_data, dtype = np.float32)

X = tf.placeholder(tf.float32, [None,2])
Y = tf.placeholder(tf.float32, [None,1])

#첫번째 유닛
W1 =tf.Variable(tf.random_normal([2,2]) , name = 'weight1')
b1 =tf.Variable(tf.random_normal([2]) , name = 'bias1')

layer1 = tf.sigmoid(tf.matmul(X, W1)+b1)

#두번째유닛
W2 =tf.Variable(tf.random_normal([2,1]) , name = 'weight2')
b2 =tf.Variable(tf.random_normal([1]) , name = 'bias2')
hypothesis = tf.sigmoid(tf.matmul(layer1,W2) + b2)

cost = -tf.reduce_mean(Y*tf.log(hypothesis) + (1-Y) * tf.log(1-hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

predicted = tf.cast(hypothesis >0.5 , dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,Y), dtype =tf.float32))

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  for step in range(20001):
    sess.run(train, feed_dict = {X:x_data , Y:y_data})
    if step % 5000 == 0:
      print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run([W1, W2]))
  h,c,a = sess.run([ hypothesis , predicted, accuracy] , feed_dict={X:x_data, Y:y_data})
  print("\nHypothesis:" ,h, "\nCorrect:" ,c , "\n정확도:" , a)

import numpy as np

A = np.array([[2000,1000],[1800,800]])
B = [[500], [500]]
C = [[800], [10000]]
result1 = np.dot(A,B)
result2 = np.dot(A,C)

print("기숙사비 ", result1[0] + result1[1])
print("등록금", result2[0] + result2[1])

import numpy as np

A = np.array([[5000,2000,1500],[2000,3000,1000]])
B = [[2],[4],[3]]
C = [[1.8],[3.5], [2.5]]
result1 = np.dot(A,B)
result2 = np.dot(A,C)

print("한국매출액 ", result1[0] , "미국매출액", result1[1])
print("한국원가 ", result2[0] , "미국원가", result2[1])
print("한국이익 ", result1[0]-result2[0] , "미국이익", result1[1]-result2[1])
print("총매출액",  (result1.flatten().sum())) #sum에 리스트이름 한개만 넣으면 거기에있는거 모두 계산되기도 함
print(sum(result1.flatten()))
print(sum(result1))
print(result1.sum())