import math as m
#EXAME 2016/2017

#Pergunta 1 - ESTUDAR!!!!,Erros

#Pergunta 2 - Newton

#x**2-y-1.2=0
#-x+y**2-1=0

def f1(x,y): 
    return x**2-y-1.2

def f2(x,y):
    return -x+y**2-1

def f1x(x,y):
    return 2*x

def f1y(x,y):
    return -1

def f2x(x,y):
    return -1

def f2y(x,y):
    return 2*y

print("Pergunta 2")
def newton(x,y):
    x1 = x - (f1(x,y)*f2y(x,y)-f2(x,y)*f1y(x,y))/(f1x(x,y)*f2y(x,y)-f2x(x,y)*f1y(x,y))
    y1 = y - (f2(x,y)*f1x(x,y)-f1(x,y)*f2x(x,y))/(f1x(x,y)*f2y(x,y)-f2x(x,y)*f1y(x,y))
    #while(abs(x-x1)>0.00001 or abs(y-y1)>0.00001):
    #como so queremos 2 iterações
    x = x1
    y = y1
    x1 = x - (f1(x,y)*f2y(x,y)-f2(x,y)*f1y(x,y))/(f1x(x,y)*f2y(x,y)-f2x(x,y)*f1y(x,y))
    y1 = y - (f2(x,y)*f1x(x,y)-f1(x,y)*f2x(x,y))/(f1x(x,y)*f2y(x,y)-f2x(x,y)*f1y(x,y))        
    print(x,y)
    print(x1,y1)
        
print(newton(1,1))

#Pergunta 3 - ESTUDAR!!!!!,Optimização

#Pergunta 4 - Corda  
def f(x):
    return x**7+0.5*x-0.5

print("Pergunta 4")
def rope(a,b):
    counter =0
    while(abs(b-a)>0.000001 and counter<3):
        m = (a*f(b)-b*f(a))/(f(b)-f(a))
        if(f(a)*f(m)<0):
            b=m
            print(b)
        else:
            a=m
            print(a)
        counter+=1
    return a

print(rope(0,0.8))
print(rope(0.8, 0.656044))

#Pergunta 5 - Euler, RK4

#dy/dt=dy/dx=z
#dy**2/dt**2=dz/dx=0.5+x**2+x*z

def ff(x,y,z): #dy/dx
    return z

def g(x,y,z): #dz/dx
    return 0.5+x**2+x*z

print("Pergunta 5")
print("Euler")
def euler(h,xo,yo,zo,b):   #h é o passo escolhido, 
                            #b limites de integração - so numa variável (x)
    counter = 0                        #xo e yo são as coordenadas do ponto incial
    while (abs(b - xo) > 0.0001 and counter <3):
        print(xo,yo,zo)
        y_ = ff(xo, yo, zo)
        z_ = g(xo, yo, zo)
        xo += h
        yo = yo + h * y_
        zo = zo + h * z_
        counter +=1
    return (yo, zo)

def quociente_convergencia(s,s_,s__,i): 
    return (s_[i]-s[i])/(s__[i]-s_[i])


def erro(ordem,s__,s_,i):
    return (s__[i]-s_[i])/(2**ordem-1)


print(euler(0.25,0,0,1,1))

print("RK4")
def rk4(h,xo,yo,zo,b):
    counter =0
    while(abs(b-xo)>0.0001 and counter<3):
        print(xo,yo,zo)
        counter +=1
        x = xo
        y = yo
        z = zo
        xo += h
        y1 = h*ff(x,y,z)
        z1 = h*g(x,y,z)
        y2 = h*ff(x+h/2, y+y1/2, z+z1/2)
        z2 = h*g(x+h/2, y+y1/2, z+z1/2)
        y3 = h*ff(x+h/2, y+y2/2, z+z2/2)
        z3 = h*g(x+h/2, y+y2/2, z+z2/2)
        y4 = h*ff(x+h,y+y3,z+z3)
        z4 = h*g(x+h,y+y3,z+z3)
        yo += y1/6+y2/3+y3/3+y4/6
        zo += z1/6+z2/3+z3/3+z4/6
    return 

print(rk4(0.25,0,0,1,1))  


#Pergunta 6 - trapezios, simpson

def l(x):
    return m.sqrt(1+(1.5*m.exp(1.5*x))**2)
    

print("Pergunta 6")
print("Trapezios")
def trapezios(a,b,h):
    sum = l(a)
    n = (b-a)/h
    natual = 1
    while(natual<n):
        sum += 2*l(a+natual*h)
        natual+=1 
    sum += l(b)
    sum *= (h/2)
    return sum, n


s = trapezios(0,2,0.5)
print(s)
s_ = trapezios(0,2,0.5/2)
print(s_)
s__ = trapezios(0,2,0.5/4)
print(s__)

print("qc:",quociente_convergencia(s, s_, s__, 0))
print("erro:",erro(2,s__,s_,0))

print("Simpson")
def simpson(a,b,h):
    sum = l(a)
    n = (b-a)/h
    natual = 1
    while(natual<n):
        if(natual%2==0):
            sum += 2*l(a+natual*h)
        else:
            sum += 4*l(a+natual*h)
        natual+=1 
    sum += l(b)
    sum *= (h/3)
    return sum

s = simpson(0,2,0.5)
print(s)
s_ = simpson(0,2,0.5/2)
print(s_)
s__ = simpson(0,2,0.5/4)
print(s__)

def qc(s,s_,s__):
    return (s_-s)/(s__-s_)

def erro(o,s_,s__):
    return (s__-s_)/(2*o-1)
    

print("qc:",qc(s, s_, s__))
print("erro: ",erro(4,s__,s_))
        



        
        
    


        
        