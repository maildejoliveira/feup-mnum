import math as m
#EXAME 2013/14

#Pergunta 1
#m(d2x/dt2)+c(dx/dt)+kx=0

#Euler - sistema de eq diferenciais

#1. dx/dt=y -> y_(x,y,z)
#2. dy/dx=(-k*y-c*z)/m -> z_(x,y,z)
#Por observação do gráfico
print("Pergunta 1.1: ", 0.1)
print("Pergunta 1.2: ", 1.0)
print("Pergunta 1.3: ", 20.0)

#Pergunta 2
#g(x)=-x+b*cos(sqrt(x))+a
print("Pergunta 2.1: ", 3)
#menor raiz real 
#intervalo mais ou menos
print("Pergunta 2.2: ")

def g(x):
    return -x+40*m.cos(m.sqrt(x))+3

def dg(x):
    return -20*m.sin(m.sqrt(x))/m.sqrt(x) -1

def newton(guess):
    counter =0
    x =  0
    while(abs(x-guess)>0.00001):
        x = guess
        if(counter<3):
            print(guess,g(guess))
        guess = guess - g(guess)/dg(guess)
        counter +=1
    return guess

print(newton(1.7))
print("Pergunta 2.2: nenhuma")

#Pergunta 3 - Gauss

#passos:
#1. A:matrix([0.1,0.5,3,0.25],[1.2,0.2,0.25,0.2],[-1,0.25,0.3,2],[2,0.00001,1,0.4]);
#2. B: matrix([0],[1],[2],[3]);
#3. AB: addcol(A,B);
#4. AB: echelon(AB);
#5. float(%);
print("Pergunta 3a) ", [1,5,30,2.5,0],[0,1,6.16379,-0.17241],[0,0,1,-0.95417,-1.41034],[0,0,0,1,1.82038])

#6. invert(A).B;
print("Pergunta 3b) ", 0.97263, -3.06443, 0.32662, 1.82038)

#7. DA:zeromatrix(4,4)+da;
#8. DB:zeromatrix(4,1)+db;
#9. X: invert(A).B;
#10. BP:DB-DA.X;
#11. invert(A).BP;
#12. estab: subst([da=0.3,db=0.3],%);
print("Pergunta 3c) ", 0.12249, 0.56700, -0.01530, 0.13437)

#Pergunta 4 
#Distinguir de m negativo e positivo

#Pergunta 5
#Aurea - pag 
print("Pergunta 5: ") 

def f(x):
    return 5*m.cos(x)-m.sin(x)

B = (m.sqrt(5)-1)/2
A = B**2

def aureamin(x1,x2,x3,x4):
    counter = 0
    while(abs(x1-x2)>0.0001):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        if(counter < 3):
            print(x1,x2,x3,x4)
            print(f(x1),f(x2),f(x3),f(x4))
        if(f(x3)<f(x4)):
            x2 = x4
        else:
            x1 = x3
        counter += 1
    return

print(aureamin(2, 4, 2.76393, 3.23606))
print(3.23606-2.76393)

#Pergunta 6 

#Pergunta 7

def func(x):
    return x**4-4*x**3+x-3

#Maxima dá duas raizes reais
print("Pergunta 7a) ", 2)
print("pelo maxima ")
print(-0.92717, 3.98444)
print("Pergunta 7b)")
#Nota: menor raiz real positiva
#logo 3.98444
print("SIM, SIM, NÃO, SIM")
#pelo maxima
print("Pergunta 7c) SIM, SIM, NÃO")

print("Pergunta 7d)")
def gpp(x):
    return (-x+4*x**3+3)**(1/4)

def pp(guess):
    counter = 0
    while(counter<3):
        print(counter, guess)
        guess = gpp(guess)
        counter += 1
        
print(pp(3.5))
        

