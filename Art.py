import turtle
import random

__Pen = turtle.Pen()


__Pen.speed(100)
for __count in range(50):
    __Pen.pendown()
    _str = random.randint(10, 100)
    for __count in range(5):
        __Pen.forward(_str)
        __Pen.right(144)
    __Pen.penup()
    __Pen.goto(random.randint((-500), 500), random.randint((-500), 500))
turtle.done()
