import numpy as np
import tensorflow as tf


x_data = [[0,0],[0,1], [1,0],[1,1]]
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
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted), dtype= tf.float32))


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(10001):
        sess.run(train, feed_dict = {X:x_data , Y:y_data})
        if step %500 == 0 :
            print(step, sess.run(cost, feed_dict = {X:x_data , Y:y_data}), sess.run(W))
            
            h,c,a = sess.run([hypothesis, predicted , accuracy], feed_dict = {X:x_data , Y:y_data})
            print("\nHyppothesis:" , h ,"\nCost:" ,c, "\nAccuaracy:", a)
            
        