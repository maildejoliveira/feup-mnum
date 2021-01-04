import math as m
#TESTE 2019-1

def func(x):
    return m.exp(x)-x+2-4

#a) Raizes intervalos:
#1. [1,3]
#2. [-1,1]

print("Pergunta 1 a)", [1,3],[-1,1])

#Recorrência para newton

print("Pergunta 1 b) x(n+1)= n(n) - f(x)/f'(x), isto é,  (m.exp(x)-x+2-4)/(m.exp(x)-1)")


def func_(x):
    return m.exp(x)-1

def recorrencia1_pp(x):
    return m.exp(x)-2-4

def recorrencia2_pp(x):
    return m.log(4+x+2)

def newton(guess):
    x= -2
    while(abs(x-guess)>0.00001):
        x = guess
        guess = guess - func(x)/func_(x)
    return guess

print(newton(0))
        


    
    