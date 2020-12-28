import math as m
#OPTIMIZAÇÃO UNIDIMENSIONAL 

#REGRA DA SECÇÃO ÁUREA - pag 184
#permite a pesquisa unidimensional de um mínimo ou máximo de uma função

#1. partimos de um intervalo fechado [x1,x2]
#2.geramos 2 pontos a cada iteração x3 e x4 sempre gerados pelas mesmas expressões
#   x3 = x1 + A*(x2-x1)
#   x4 = x2 + B*(x2-x1)
#3. temos dois algoritmos um para o minimo e outro para o máximo

#razão áurea = (sqrt(5)-1)/2 
#B = razão áurea
#A = B**2

B = (m.sqrt(5)-1)/2
A = B**2

def f(x):
    return -5*m.cos(10*x)+(2*x**2)+1

#Critério de paragem: |x1-x2| <= erro

def aurea_minimo(x1,x2):
    while(abs(x1-x2)>0.0001):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        if(f(x3)<f(x4)):
            x2=x4
        else:
            x1=x3
    return x1

def aurea_maximo(x1,x2):
    while(abs(x1-x2)>0.0001):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        if(f(x3)<f(x4)):
            x1=x3
        else:
            x2=x4
    return x1

print(aurea_maximo(-1,0))
print(aurea_minimo(-1,0))