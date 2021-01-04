import math as m

#INTEGRAÇÃO DE INTEGRAIS DEFINIDOS SIMPLES

def f(x):
    return m.sin(x)/(x**2)

#REGRA DOS TRAPÉZIOS - pag 112
#METODO DE 2ªORDEM

def trapezios(n,a,b): #a e b são os limites de integração e n o numero de trapezios
    h = (b-a)/n #h é o passo
    n_atual = 1
    area=f(a)
    xo=a
    while(n_atual < n):
        area+=2*f(xo + n_atual*h)
        n_atual+=1
    area += f(b)
    area = area*(h/2)
    return area

#PERGUNTAS TÍPICAS:
#1. Calcule o integral pelo método numérico: Trapézios e Simpson
#2. O passo escolhido é adequado? - implica calcular QUOCIENTE DE CONVERGÊNCIA
#3. Estima o erro para cada um dos métodos - implica calcular o ERRO

#QUOCIENTE DE CONVERGÊNCIA
#este é calculado para se perceber q mediante a ordem do metodo toma valores adequados
#respetivamente s,s_ e s__ são a resolução do método com ninicial, ninicial*2, ninicial*4
#consequentemente estão a dividir o passo (h) por 2, calculando para intervalos mais pequenos
#Vê se estamos a ter valores corretos se QC=2^ordem do metodo (aproximadamente)
#Formula: (s_-s)/(s__-s_)

def quociente_convergencia(s,s_,s__): 
    return (s_-s)/(s__-s_)

#ERRO
#Formula: (s__-s_)/(2**ordem-1)

def erro(ordem,s__,s_):
    return (s__-s_)/(2**ordem-1)


print("Exemplo:")
s=trapezios(4,m.pi/2,m.pi)
s_=trapezios(8,m.pi/2,m.pi)
s__=trapezios(16,m.pi/2,m.pi)
print(s,s_,s__)
print(quociente_convergencia(s, s_, s__))
print(erro(2, s__, s_))
