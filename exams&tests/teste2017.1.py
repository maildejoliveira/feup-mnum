import math as m 

def f(x):
    return (x-3.6)+m.cos(x+1.2)**3


def f_(x):
    return 1-3*(m.cos(x+1.2)**2)*m.sin(x+1.2)

def newton(guess):
    x = -1
    n = 0
    while(abs(x-guess)>0.0001):
        if(n <2):
            print(guess)
        x = guess
        guess = x - f(x)/f_(x)
        
    return guess
    
newton(0.5)