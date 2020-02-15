# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13rYXSyFNtH-1wA2sXB8UV0tDaoa-4Kr9
"""

hello = tf.constant("Hello world!")
sess = tf.Session()
print(sess.run(hello))
sess.close()

node1 = tf.constant(7, dtype= tf.int32)
node2 = tf.constant(2, dtype= tf.int32)
sess = tf.Session()
print(sess.run([node1, node2]))

#텐서플로우의 자료형 3개
#1.constant   --> 변하지 않는 값. 정수 실수 상관없음. 문자열을 넣을수있다 . 미리넣는것
#2.placeholder  -->나중에 내가 원하는 값을 텐서에 넣어주겠다
#3.Variable   -->

hello = tf.constant('Hello. Tensorflow')
#constant = 노드(==텐서) 를 하나 정의하겠다
#노드에 문자열을 넣은 변수 hello를 선언하겠다


sess = tf.Session()
print(sess.run(hello))
print(sess.run(a+b))

#1. 계산그래프 생성

hello = tf.constant('hello TF')
sess= tf.Session()
print(sess.run(hello))
a = tf.constant(10)
b = tf.constant(32)
c = tf.add(a,b)

#세션실행
print(sess.run(a+b))
print(sess.run(c))

sess.close()

a = tf.constant(10)
b = tf.constant(20)
sum = a+b
min = a-b
mul = a*b
dvi = a/b

sess= tf.Session()
print("1.덧셈) a+b =" , sess.run(sum))
print("2.뺄셈) a-b =" , sess.run(min))
print("3.곱셈) a*b =" , sess.run(mul))
print("4.나눗셈) a/b =" , sess.run(dvi))
sess.close()    #그래프 생성 종료

#먼저 빈 노드만 생성해놓고, 나중에 값을 넣겠다는 의미의 placeholder.
#자바의 Scanner 같은거라고 보면됨

a = tf.placeholder(tf.int32)  #빈 텐서를 만들어놓음 , 타입은 써줘야함
b = tf.placeholder(tf.int32)
add=a+b

sess=tf.Session()   
print(sess.run(add, feed_dict={a:3 , b:4}))  #빈텐서에 값을넣음. 딕셔너리 형식
print(sess.run(add, feed_dict={a:[1,2] , b:[3,4]}))     #딕셔너리형식의 리스트형태
print(sess.run(add, feed_dict={a:[[1,2],[3,4]], b:[[5,6],[7,8]]}))
sess.close()

#Variable -> 계속 변화하는 값을 위해 설정해준다.

sess= tf.Session()

var1 = tf.Variable([5])
var2 = tf.Variable([10])
var3 = tf.Variable([3])

var4 = var1 + var2 + var3

init = tf.global_variables_initializer() #배리어블은 이 과정을 거쳐 꼭 초기화를 해줘야한다
sess.run(init)

result = sess.run(var4)
print(result)



