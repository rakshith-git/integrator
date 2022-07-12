from turtle import *
from math import *
from time import *
tracer(0)
speed(0)


#for 2 solutions of square root set dsoln as True
sqrtcase='false'
dsoln=True
lowerlim=-3
upperlim=3
dx=0.01
a=50
sh=1





def func(x):
        global sqrtcase
        try:
            # enter your function
            
            function=3*(sqrt(1-x*x/4))
            
            
            
            return(function)
        except:
        	sqrtcase='true'
        	return(0)
        else:
        	sqrtcase='false'
        	
        
def rect(l,b,x):
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

t=Turtle()
t.setpos(-300,-300)
color('black','black')
sc=Screen()
sc.screensize(5000,5000)
s=Turtle()
s.color('red3')
for i in range(-1,2):
	s.goto(i*3000,0)
s.home()
for i in range(-1,2):
	s.goto(0,i*3000)

s.shapesize(0.1,5)
s.shape('square')
s.pu()
area=0
x=lowerlim
y1,y2=0.0,0.0
adx=[dx*20,dx*10,dx]

while x<=upperlim:
    area+=(dx*func(x))
    x+=dx
    y1=a*func(x)
    dy=y2-y1
    rect(a*func(x),dx*a,(a*x)/sh)
    if sqrtcase == 'true' and dsoln==True:
        rect(-a*func(x),dx*a,(a*x)/sh)
        area+=abs(dx*func(x))
    s.setpos((a*x)/sh,a*func(x))
    y2=y1
    s.seth(degrees(-atan((dy/dx/a)*sh)))
    t.clear()
    t.write("area="+str("{:.4f}".format(area))+"    slope="+str(round(degrees(-atan((dy/dx/a)*sh)),2)))
    update()
 
sleep(100)