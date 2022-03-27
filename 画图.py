import turtle as a
import random as b

a.screensize(400, 400, "green")
a.setup()
a.speed(8)


def my_zuobiaoxi():
    a.pencolor("black")
    a.pensize(3)
    a.penup()
    a.goto(0, 400)
    a.pendown()
    a.goto(0, -400)
    a.penup()
    a.goto(-500, 0)
    a.pendown()
    a.goto(500, 0)
    a.pensize(10)


def my_goto(x, y):
    a.penup()
    a.goto(x, y)
    a.pendown()


my_zuobiaoxi()
a.pensize(10)
my_goto(-100, -100)

for j in range(3, 100):
    print(j)
    if (360 % j) == 0:
        a.pencolor(b.random(), b.random(), b.random())
        for i in range(j):
            a.fd(200)
            a.left(360 / j)

'''
for i in range(3):
    a.fd(200)
    a.left(120)
for i in range(4):
    a.fd(200)
    a.left(90)
for i in range(5):
    a.fd(200)
    a.left(72)
for i in range(6):
    a.fd(200)
    a.left(60)
my_goto(-200,-200)
for i in range(4):
    a.fd(400)
    a.left(90)
'''
