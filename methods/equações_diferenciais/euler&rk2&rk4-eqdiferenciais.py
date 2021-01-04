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

#INTEGRAÇÃO NUMÉRICA DE EQUAÇÕES DIFERENCIAIS
#dy/dx=y'=f(x,y)

#PERGUNTAS:
#Resolva a equação diferencial para cada um dos métodos
#Calcule o quociente de convergência, o passo escolhido é adequado?
#Calcule o erro

def f(x,y):
    return x**2+y**2

#METODO DE EULER
#metodo de 1ªOrdem

#Formula de Recorrência:
#   xn+1=xn+h
#   yn+1=yn+h*y'    (y'=f(xn,yn))

def euler(h,xo,yo,a,b): #h é o passo escolhido, 
                        #a e b limites de integração - so numa variável (x)
                        #xo e yo são as coordenadas do ponto incial
    while (abs(b - xo) > 0.0001):
        y_ = f(xo, yo)
        xo += h
        yo = yo + h * y_
    return yo

print("EXEMPLO EULER:")
s=euler(0.1,0,0,0,1.4)
s_=euler(0.05,0,0,0,1.4)
s__=euler(0.025,0,0,0,1.4)
print(s,s_,s__)

print("QC:", quociente_convergencia(s, s_, s__))
print("ERRO:", erro(1,s_,s__))


def rk2(h,xo,yo,a,b):   #h é o passo escolhido, 
                        #a e b limites de integração - so numa variável (x)
                        #xo e yo são as coordenadas do ponto incial
    while abs(b - xo) > 0.00001:
        x = xo
        y = yo
        xo = x + h
        yo = y + h * f(x + h/2, y + h/2 * f(x, y))
    return yo

print("EXEMPLO RK2:")
s=rk2(0.1,0,0,0,1.4)
s_=rk2(0.05,0,0,0,1.4)
s__=rk2(0.025,0,0,0,1.4)
print(s,s_,s__)

print("QC:", quociente_convergencia(s, s_, s__))
print("ERRO:", erro(2,s_,s__))


def rk4(h,xo,yo,a,b):   #h é o passo escolhido, 
                        #a e b limites de integração - so numa variável (x)
                        #xo e yo são as coordenadas do ponto incial
    while abs(b - xo) > 0.00001:
        x = xo
        y = yo
        xo = x + h
        y1 = h*f(x,y)
        y2 = h*f(x+h/2,y+y1/2)
        y3 = h*f(x+h/2,y+y2/2)
        y4 = h*f(x+h,y+y3)
        yo = y + y1/6 + y2/3 + y3/3 + y4/6
    return yo

print("EXEMPLO RK4:")
s=rk4(0.1,0,0,0,1.4)
s_=rk4(0.05,0,0,0,1.4)
s__=rk4(0.025,0,0,0,1.4)
print(s,s_,s__)

print("QC:", quociente_convergencia(s, s_, s__))
print("ERRO:", erro(4,s_,s__))
        
