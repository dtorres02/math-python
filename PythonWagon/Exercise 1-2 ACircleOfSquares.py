'''
Exercise 1-2: A Circle of Squares
    Write and run a function that draws 60 squares, turning right 5 degrees after each square.
    Use a loop!
'''

from turtle import *

### Square Function
def square(length):
    for i in range(4):
        forward(length)
        right(90)


### Circle of Squares
for i in range(60):
    square(100)
    right(5)