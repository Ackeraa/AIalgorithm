from __future__ import print_function
import tensorflow.compat.v1 as tf
import os

tf.disable_v2_behavior()

a = tf.constant(5.0, name = "a")
b = tf.constant(10.0, name = "b")

x = tf.add(a, b, name = "add")
y = tf.div(a, b, name = "divide")

with tf.Session() as sess:
    writer = tf.summary.FileWriter("./", sess.graph)
    print("output: ", sess.run([a, b, x, y]))  
writer.close()    
sess.close()
