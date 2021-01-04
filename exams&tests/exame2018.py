import math as m 
#Exame 2018/2019

#Pergunta 1
#metodo de Newton para sistemas não lineares - pag 68
#f(x,y)=0
#g(x,y)=0
print("Pergunta 1: ")

def ff(x,y):
    return m.sin(x+y)-m.exp(x-y)

def gg(x,y):
    return m.cos(x+y)-x**2*y**2

def ff_x(x,y):
    return m.cos(x+y)-m.exp(x-y)

def ff_y(x,y): 
    return m.cos(x+y)+m.exp(x-y)

def gg_x(x,y):
    return -m.sin(x+y)-2*x*y**2

def gg_y(x,y):
    return -m.sin(x+y)-2*y*x**2

def newton_nl(x,y):
    xo = 0
    yo = 0
    counter = 0
    while(abs(xo-x)>0.00001 or abs(yo-y)>0.0001):
        xo = x
        yo = y
        if(counter < 3):
            print(xo,yo)
        jac = ff_x(x,y)*gg_y(x,y)-ff_y(x,y)*gg_x(x,y)
        hx = (ff(x,y)*gg_y(x,y)-gg(x,y)*ff_y(x,y))/jac
        hy = (ff_x(x,y)*gg(x,y)-gg_x(x,y)*ff(x,y))/jac
        x = xo - hx
        y = yo - hy
        counter += 1
    return x, y
        
print(newton_nl(0.5,0.25))


print("Pergunta 2: ")
print("a) I")
print("b) todas")
print("c)")
print("xn+1 = (1.2 - 6.1yn -41zn)/103")
print("yn+1 = (0 - 5.5xn+1 -3zn)/5.5")
print("zn+1 = (-13 - 2xn+1 -10yn+1)/13")

def cubaturaSimpson():
    e0 = 7.8 + 1.1 + 9.8 + 1.2
    e1 = 2.1 + 1.4 + 2.2 + 1.5
    e2 = 4
    hx = 2/2
    hy = 2/2
    sum = (hx*hy)*(e0 + 4*e1 + 16* e2)/9
    return sum

print("Pergunta 3: ", cubaturaSimpson())

print("Pergunta 4: ")
def f(x,y,z):
    return z

def g(x,y,z):
    return -7*z-4*y

def euler(xo,yo,zo,h):
    counter = 0
    while(counter<4):
        print(xo,yo,zo)
        counter +=1
        deltay = h*f(xo,yo,zo)
        deltaz = h*g(xo,yo,zo)
        xo += h
        yo += deltay
        zo += deltaz
        
print(euler(0.4,2.0,1.0,0.2))

def func(x):
    return (x-2)**2+x**4

B = (m.sqrt(5)-1)/2
A = B**2

def aurea_min(x1,x2):
    while(abs(x1-x2)>0.00001):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        if(func(x3)<func(x4)):
            x2 = x4
        else:
            x1 = x3
    return x1

print("Pergunta 5: ",aurea_min(0,2))
        