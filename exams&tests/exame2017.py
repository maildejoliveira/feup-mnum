import math as m
#EXAME 2017/2018

#Pergunta 1 - Minímo da função (minimizar/pesquisa unidimensional)
#f: (x-4)**2+x**4;
#plot2d(f,[x,0,2]);

#Opções de Resolução:
#1. Método dos terços, exige muito cálculo da função f e escolha de divisão do intervalo
#2. Regra Áurea
#3. ?
#4. ?

def h(x):
    return (x-4)**2+x**4

B = (m.sqrt(5)-1)/2
A = B**2

def aurea(x1,x2):
    while(abs(x1-x2)>0.0000001):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        if(h(x3)<h(x4)):
            x2 = x4
        else:
            x1 = x3
    return x1

print("Resposta P1 Aurea:", aurea(0,2))

#Pergunta 5 - Trapezios e Simpson

#y=f(x)
#y=exp(k*x)
#L = integrate(sqrt(1+y_**2),a,b)
#a = 0
#b = 1
#k = 2.5
#h = 0.125

def f(x):
    return m.sqrt(1+(2.5*m.exp(2.5*x))**2)

def trapezios(a,b,h):
    n = (b-a)/h
    natual = 1
    sum = f(a)
    while(natual < n):
        a += h
        sum += 2*f(a)
        natual += 1
    sum += f(b)
    sum *= (h/2)
    return sum


def simpson(a,b,h):
    n = (b-a)/h
    natual = 1
    sum = f(a)
    while(natual <n):
        a += h
        if(natual%2==0):
            sum += 2*f(a)
        else:
            sum += 4*f(a)
        natual+=1
    sum += f(b)
    sum *= (h/3)
    return sum

print("Resposta P2 h:", 0.125,0.125)
print("Resposta P2 h'':", 0.125/2,0.125/2)
print("Resposta P2 h''':", 0.125/4,0.125/4)
print("Resposta P2 L1: ",trapezios(0,1,0.125),simpson(0,1,0.125))
print("Resposta P2 L2: ",trapezios(0,1,0.125/2),simpson(0,1,0.125/2))
print("Resposta P2 L3: ",trapezios(0,1,0.125/4),simpson(0,1,0.125/4))

def quociente(s,s_,s__):
    return (s_-s)/(s__-s_)

def erro(s_,s__,ordem):
    return (s__-s_)/(2**ordem-1)

print("Resposta P2 QC: ",quociente(trapezios(0,1,0.125), trapezios(0,1,0.125/2),trapezios(0,1,0.125/4)), quociente(simpson(0,1,0.125), simpson(0,1,0.125/2),simpson(0,1,0.125/4)))
print("Resposta P2 ER: ",erro(trapezios(0,1,0.125/2),trapezios(0,1,0.125/4),2), erro(simpson(0,1,0.125/2),simpson(0,1,0.125/4),4))

#Pergunta 3 - PicardPeano
#função f: m.exp(x)-x-5

#Formula de Recorrência 1: xn+1 = m.exp(xn)-5
#Formula de Recorrência 2: xn+1 = m.log(5+xn)

#Passos no Máxima:
#1. fpp: exp(x)-x-5;
#2. plot2d(fpp,[x,-6,3]);
#temos 2 raízes x1-[-6,-4] e x2-[1,3]

#Avaliar as FR para cada uma das raízes
#para x1: Formula de Recorrência 1 pois o modulo da derivada no intervalo é menor que 1
#para x2: Formula de Recorrência 2 pois o modulo da derivada no intervalo é menor que 1

def recorrencia1(x):
    return m.exp(x)-5

def recorrencia2(x):
    return m.log(5+x)

def picardpeano1(guess):
    x = 0
    while(abs(x-guess)>0.000001):
        x = guess
        guess = recorrencia1(x)
    return guess
        
def picardpeano2(guess):
    x = 0
    counter = 0
    while(abs(x-guess)>0.000001):
        x = guess
        guess = recorrencia2(x)
        counter += 1
    return guess, counter

print("Resposta P3 x1-[-6,-4] PP guess=-5:", picardpeano1(-5))
print("Resposta P3 x2-[1,3] PP guess=2:", picardpeano2(2))

def y(x):
    return m.exp(x)-x-5

def y_(x):
    return m.exp(x)-1
    

def newton(guess):
    x = 0
    counter=0 
    while(abs(x-guess)>0.000001):
        x = guess
        guess = x - y(x)/y_(x)
        counter += 1
    return guess, counter

print("Resposta P3 x2-[1,3] Newton guess=2:", newton(2))


#Pergunta 4 - Sistema de equações diferenciais (Euler)

#dC/dt = -m.exp(-0.5/(T+273))*C - f1(t,C,T)
#dT/dt = 30*m.exp(-0.5/(T+273))*C-0.5*(T-20) - f2(t,C,T)

def f1(t,C,T):
    return -m.exp(-0.5/(T+273))*C

def f2(t,C,T):
    return 30*m.exp(-0.5/(T+273))*C-0.5*(T-20)

def euler(to,Co,To,n,h,tf):
    natual = 0
    while(abs(to-tf)>0.00001):
        if(natual<n):
            print(to,Co,To)
        f1_ = f1(to,Co,To)
        f2_ = f2(to,Co,To)
        to += h
        Co += h*f1_
        To += h*f2_
        natual += 1
    return Co,To
        
print("Resposta P4a)Euler:")      
print(euler(0,2.5,25,3,0.25,0.5))

def rk4(to,Co,To,n,h):
    natual = 0
    while(natual<n):
        print(to,Co,To)
        y1 = h*f1(to,Co,To)
        z1 = h*f2(to,Co,To)
        y2 = h*f1(to+h/2,Co+y1/2,To+z1/2)
        z2 = h*f2(to+h/2,Co+y1/2,To+z1/2)
        y3 = h*f1(to+h/2,Co+y2/2,To+z2/2)
        z3 = h*f2(to+h/2,Co+y2/2,To+z2/2)
        y4 = h*f1(to+h,Co+y3,To+z3)
        z4 = h*f2(to+h,Co+y3,To+z3)     
        f1_ = y1/6+y2/3+y3/3+y4/6
        f2_ = z1/6+z2/3+z3/3+z4/6
        to += h
        Co += f1_
        To += f2_
        natual += 1
        
print("Resposta P4b)RK4:")      
print(rk4(0,2.5,25,3,0.25))

def quociente(s,s_,s__):
    return (s_-s)/(s__-s_)

def erro(s_,s__,ordem):
    return (s__-s_)/(2**ordem-1)

print("Resposta P4c):")  
print("QC:", quociente(euler(0,2.5,25,3,0.25,0.5)[0],euler(0,2.5,25,3,0.25/2,0.5)[0],euler(0,2.5,25,3,0.25/4,0.5)[0]))
print("Erro: ", erro(euler(0,2.5,25,3,0.25/2,0.5)[0],euler(0,2.5,25,3,0.25/4,0.5)[0],1))


#Pergunta 5 - Mínimo da função Gradiente

def w(x,y):
    return -1.1*x*y+12*y+7*x**2-8*x

def gradiente(x,y):
    return -1.1*y+14*x-8, 12-1.1*x

def gradiente_method(n,h,xo,yo):
    counter = 0
    (x,y)=(0,0)
    while(counter<n):
        (x,y)=(xo,yo)
        (xo,yo)=(x-h*gradiente(x,y)[0],y-h*gradiente(x,y)[1])
        counter += 1
    return xo,yo

print("Resposta P5:",w(gradiente_method(1, 0.1, 3, 1)[0],gradiente_method(1, 0.1, 3, 1)[1]))
        

        
    

    
    
