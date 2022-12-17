from turtle import *
from math import *
from time import *

tracer(0)
speed(0)

# for 2 solutions of square root set dsoln as True
sqrtcase = "true"
dsoln = False
lowerlim = -3.14
upperlim = 3.14
dx = 0.01
a = 100
sh = 1
l = 3.1415 / 2

pi = 3.1415


def func(x):
    global sqrtcase, xd
    sol = 0
    tt = 0
    for i in range(1, 50, 2):
        tt += 1
        sol += (1 / i) * (sin((i * pi * x) / l))
    try:
        # enter your function in terms of 'y'

        function = (4 / pi) * sol

        return function
    except:
        sqrtcase = "true"
        return 0
    else:
        sqrtcase = "false"


lol = -7
g = Turtle()
g.speed(0)
g.color("blue3")
g.pu()
while lol <= 7:

    if dsoln == False:
        lol = lol + 0.001
        g.goto((a * lol) / sh, a * func(lol))
        g.pd()

    if dsoln == True:
        lol += 0.01
        g.pu()
        g.goto((a * lol) / sh, a * func(lol))
        g.pd()
        g.fd(1)
        g.bk(1)
        g.pu()
        g.goto((a * lol) / sh, -a * func(lol))
        g.pd()
        g.fd(1)
        g.bk(1)
g.ht()


def rect(l, b, x):
    pu()
    setx(x)
    pd()
    seth(90)
    begin_fill()
    for i in range(2):
        fd(l)
        rt(90)
        fd(b)
        rt(90)
    end_fill()


t = Turtle()
t.setpos(-300, -300)
color("black", "black")
sc = Screen()
sc.screensize(100, 500)
s = Turtle()
s.color("red3")
for i in range(-1, 2):
    s.goto(i * 3000, 0)
s.home()
for i in range(-1, 2):
    s.goto(0, i * 3000)

s.shapesize(0.1, 5)
s.shape("square")
s.pu()
area = 0
x = lowerlim
y1, y2 = 0.0, 0.0
adx = [dx * 20, dx * 10, dx]
pu()
goto(lowerlim, 0)
n = 0
while x <= upperlim:
    area += dx * func(x)
    x += dx
    y1 = a * func(x)
    dy = y2 - y1
    rect(y1, dx * a, (a * x) / sh)
    if sqrtcase == "true" and dsoln == True:
        rect(-y1, dx * a, (a * x) / sh)
        area += abs(dx * func(x))
    s.setpos((a * x) / sh, y1)
    y2 = y1
    ang = degrees(-atan((dy / dx / a) * sh))
    s.seth(ang)
    t.clear()
    t.write(
        "area="
        + str("{:.4f}".format(area))
        + "                   slope="
        + str(round(ang, 2))
    )
    update()

exitonclick()
sleep(100)
