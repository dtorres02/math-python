'''
Exercise 1-3: Tri and Tri Again
    Write a triangle() function that will draw a triangle of a given "side length".
'''

from turtle import *

### Triangle Function
### @param int length

def triangle(length = 100):
    angle = 60
    for i in range(3):
        forward(length)
        right(angle)
        angle = angle 



triangle()