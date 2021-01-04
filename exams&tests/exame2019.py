import math as m
#Exame 2019

#1 raíz
print("P1 a)",1)
print("P1 b)",[-1,0])
print("P1 c)")

def f(x):
    return m.sin(x)+x**5-0.2*x+1

def bissec(a,b):
    n = 0
    while(abs(a-b)>0.0000001):
        m = (a+b)/2
        if(f(a)*f(m)<0):
            b = m
        else:
            a = m
        if(n==5):
             print(m)    
        n+= 1
    return m


bissec(-1,0)

print("P2:")

def f1(x,y):
    return  x**2-y-1.2

def f2(x,y):
    return -x+y**2-1

def f1_x(x,y):
    return 2*x

def f1_y(x,y):
    return -1

def f2_x(x,y):
    return -1

def f2_y(x,y):
    return 2*y


def newton(x,y):
    n = 0
    while(n<3):
        print(x,y)
        jac = f1_x(x,y)*f2_y(x,y)-f2_x(x,y)*f1_y(x,y)
        xinc = (f1(x,y)*f2_y(x,y)-f2(x,y)*f1_y(x,y))/jac
        yinc = (f2(x,y)*f1_x(x,y)-f1(x,y)*f2_x(x,y))/jac
        x = x - xinc
        y = y - yinc
        n += 1
    return 

newton(1,1)

print("P3")

def ff(x):
    return m.sqrt(1+2.25*m.exp(3*x))
        
def trap(xo,xf,h):
    sum = ff(xo)
    while(abs(xo-xf)>h):
        xo += h
        sum += 2*ff(xo)
    sum += ff(xf) 
    s = sum * (h/2)
    return s


def simp(xo,xf,h):
    sum = ff(xo)
    n = 1
    while(abs(xo-xf)>h):
        xo += h
        if(n%2!=0):
            sum += 4*ff(xo)
        else:
            sum += 2*ff(xo)
        n += 1
    sum += ff(xf) 
    s = sum * (h/3)
    return s


def qc(s,s_,s__):
    return (s_-s)/(s__-s_)

def erro(s_,s__,o):
    return (s__-s_)/(2**o-1)



print("h:",0.25,0.25)
print("h':",0.25/2,0.25/2)
print("h'':",0.25/4,0.25/4)
print("L:",trap(0,2,0.25),simp(0,2,0.25))
print("L':",trap(0,2,0.25/2),simp(0,2,0.25/2))
print("L''':",trap(0,2,0.25/4),simp(0,2,0.25/4))
print("QC:",qc(trap(0,2,0.25),trap(0,2,0.25/2),trap(0,2,0.25/4)),qc(simp(0,2,0.25),simp(0,2,0.25/2),simp(0,2,0.25/4)))
print("e:",erro(trap(0,2,0.25/2),trap(0,2,0.25/4),2),erro(simp(0,2,0.25/2),simp(0,2,0.25/4),4))

print("P4")

def Temp(t,T):
    return -0.25*(T-59)

def euler(to,To,h):
    n = 0
    while(n<2):
        t = to
        T = To
        to += h
        To += h*Temp(t,T)
        n += 1
    return To

print(euler(2,2,0.5))

print("P5")

def yaurea(x):
    return -5*m.cos(x)+m.sin(x)+10

B = (m.sqrt(5)-1)/2
A = B**2

def aurea(x1,x2):
    n = 0
    a = 0
    while(n<3):
        n+= 1
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        print("x:",x1,x2,x3,x4)
        print("f:",yaurea(x1),yaurea(x2),yaurea(x3),yaurea(x4))
        if(yaurea(x3)>yaurea(x4)):
            x2 = x4  
            a = x4-x1
        else:
            x1 = x3 
            a = x3-x2
    return a

print(aurea(2,4))


print("P6")

def Z(x,y):
    return 3*x**2-x*y+11*y+y**2-8*x

def grad(x,y):
    return -y+6*x-8, 2*y-x+11

def met_grad(x,y,h):
    n = 0
    while(n<2):
        print(x,y,Z(x,y),grad(x,y),h)
        xx = x
        yy = y
        n += 1
        x = xx - h*grad(xx,yy)[0]
        y = yy - h*grad(xx,yy)[1]
        if(Z(x,y)<Z(xx,yy)):
            h*=2
        else:
            h/=2
    return 

met_grad(2,2,1)

    


    



