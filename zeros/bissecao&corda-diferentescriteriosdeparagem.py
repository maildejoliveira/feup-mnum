import math

#PESQUISA DE ZEROS REAIS DE UMA FUNÇÃO REAL
#cap2
#metodos para descobrir zeros de uma função
#metodos intervalares
#Método da Bisseção (pag 51) e Método da Corda (pag 55)

#1.ver função no máxima
#2.quantas raízes tem?
#3.isolar cada uma das raízes == delimitar um intervalo
#4.aplicar os metodos
#5.análise crítica dos resultados: rapidez, precisão e convergência
#6.fazer variar amplitude do intervalo (a-b) e os diferentes critérios

#define a tua função
def f(x):
    return x-2*math.log(x)-5

#criterio de precisao absoluta
def bissec_absolutstop(a,b):
    counter =0
    while(abs(b-a)>0.000001):
        m = (a+b)/2
        if(f(a)*f(m)<0):
            b=m
        else:
            a=m
        counter+=1
    print(counter)
    return a

#criterio de anulação da raiz
def bissec_nullfunction(a,b):
    counter =0
    while(abs(f(b)-f(a))>0.000001):
        m = (a+b)/2
        if(f(a)*f(m)<0):
            b=m
        else:
            a=m
        counter+=1
    print(counter)
    return a

#criterio de precisao absoluta
def rope_absolutstop(a,b):
    counter =0
    while(abs(b-a)>0.000001):
        m = (a*f(b)-b*f(a))/(f(b)-f(a))
        if(f(a)*f(m)<0):
            b=m
        else:
            a=m
        print(a,b)
        counter+=1
    print(counter)
    return a

#criterio de anulação da raiz
def rope_nullfunction(a,b):
    counter =0
    while(abs(f(b)-f(a))>0.000001):
        m = (a*f(b)-b*f(a))/(f(b)-f(a))
        if(f(a)*f(m)<0):
            b=m
        else:
            a=m
        counter+=1
    print(counter)
    return a   


print("EXEMPLO:")
    
print("primeira raiz")

print(bissec_absolutstop(0.01, 1.00))
print(bissec_nullfunction(0.01, 1.00))

print(rope_absolutstop(0.01, 1.00))
print(rope_nullfunction(0.01, 1.00))

print("segunda raiz")

print(bissec_absolutstop(9.0, 10.00))
print(bissec_nullfunction(9.0, 10.00))

print(rope_absolutstop(9.0, 10.00))
print(rope_nullfunction(9.0, 10.00))


