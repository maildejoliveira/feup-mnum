#QUOCIENTE DE CONVERGÊNCIA
#este é calculado para se perceber q mediante a ordem do metodo toma valores adequados
#respetivamente s,s_ e s__ são a resolução do método com ninicial, ninicial*2, ninicial*4
#consequentemente estão a dividir o passo (h) por 2, calculando para intervalos mais pequenos
#Vê se estamos a ter valores corretos se QC=2^ordem do metodo (aproximadamente)
#Formula: (s_-s)/(s__-s_)

def quociente_convergencia(s,s_,s__,i): 
    return (s_[i]-s[i])/(s__[i]-s_[i])

#ERRO
#Formula: (s__-s_)/(2**ordem-1)

def erro(ordem,s__,s_,i):
    return (s__[i]-s_[i])/(2**ordem-1)


#INTEGRAÇÃO NUMÉRICA DE SISTEMAS DE EQUAÇÕES DIFERENCIAIS
#dy/dx=y'=f(x,y,z)  dz/dx=z'=g(x,y,z)

#PERGUNTAS:
#Resolva o sistema de equações diferenciais para cada um dos métodos
#Calcule o quociente de convergência, o passo escolhido é adequado?
#Calcule o erro

def f(x,y,z):
    return z*y +x

def g(x,y,z):
    return z*x +y

#METODO DE EULER
#metodo de 1ªOrdem

#Formula de Recorrência:
#   xn+1=xn+h
#   yn+1=yn+h*y'    (y'=f(xn,yn,zn))
#   zn+1=zn+h*z'    (z'=g(xn,yn,zn))

def euler(h,xo,yo,zo,b):   #h é o passo escolhido, 
                            #b limites de integração - so numa variável (x)
                            #xo e yo são as coordenadas do ponto incial
    while (abs(b - xo) > 0.0001):
        y_ = f(xo, yo, zo)
        z_ = g(xo, yo, zo)
        xo += h
        yo = yo + h * y_
        zo = zo + h * z_
    return (yo, zo)

print("EXEMPLO EULER:")
s=euler(0.1,0,1,1,0.5)
print(s)
s_=euler(0.1/2,0,1,1,0.5)
print(s_)
s__=euler(0.1/4,0,1,1,0.5)
print(s__)
print("QC para y: ",  quociente_convergencia(s, s_, s__,0))
print("QC para z: ",  quociente_convergencia(s, s_, s__,1))
print("Erro para y: ", erro(1,s__,s_,0))
print("Erro para z: ", erro(1,s__,s_,1))


def rk2(h,xo,yo,zo,b):   #h é o passo escolhido, 
                        #b limites de integração - so numa variável (x)
                        #xo e yo são as coordenadas do ponto incial
    while abs(b - xo) > 0.00001:
        x = xo
        y = yo
        z = zo
        xo += h
        yo = yo + h * f(x + (h/2), y + (h/2) * f(x, y, z), z + (h/2) * g(x, y, z))
        zo = zo + h * g(x + (h/2), y + (h/2) * f(x, y, z), z + (h/2) * g(x, y, z))
    return (yo, zo)

print("EXEMPLO RK2:")
s=rk2(0.1,0,1,1,0.5)
print(s)
s_=rk2(0.1/2,0,1,1,0.5)
print(s_)
s__=rk2(0.1/4,0,1,1,0.5)
print(s__)
print("QC para y: ",  quociente_convergencia(s, s_, s__,0))
print("QC para z: ",  quociente_convergencia(s, s_, s__,1))
print("Erro para y: ", erro(2,s__,s_,0))
print("Erro para z: ", erro(2,s__,s_,1))



def rk4(h,xo,yo,zo,b):
    while(abs(b-xo)>0.0001):
        x = xo
        y = yo
        z = zo
        xo += h
        y1 = h*f(x,y,z)
        z1 = h*g(x,y,z)
        y2 = h*f(x+h/2, y+y1/2, z+z1/2)
        z2 = h*g(x+h/2, y+y1/2, z+z1/2)
        y3 = h*f(x+h/2, y+y2/2, z+z2/2)
        z3 = h*g(x+h/2, y+y2/2, z+z2/2)
        y4 = h*f(x+h,y+y3,z+z3)
        z4 = h*g(x+h,y+y3,z+z3)
        yo += y1/6+y2/3+y3/3+y4/6
        zo += z1/6+z2/3+z3/3+z4/6      
    return yo,zo

h1 = 0.1
print("EXEMPLO RK4:")
s=rk4(h1,0,1,1,0.5)
print(s)
s_=rk4(h1/2,0,1,1,0.5)
print(s_)
s__=rk4(h1/4,0,1,1,0.5)
print(s__)
print("QC para y: ",  quociente_convergencia(s, s_, s__,0))
print("QC para z: ",  quociente_convergencia(s, s_, s__,1))
print("Erro para y: ", erro(4,s__,s_,0))
print("Erro para z: ", erro(4,s__,s_,1))


#NOTA IMPORTANTE:
#Caso não se verifique a igualdade no QC dependendo da ordem do método 
#é necessário continuar a dividir o h e calcular de novo QC 
#(como neste caso em RK4)

h2 = h1/2
print("EXEMPLO RK4 (2):")
s=rk4(h2,0,1,1,0.5)
print(s)
s_=rk4(h2/2,0,1,1,0.5)
print(s_)
s__=rk4(h2/4,0,1,1,0.5)
print(s__)
print("QC para y: ",  quociente_convergencia(s, s_, s__,0))
print("QC para z: ",  quociente_convergencia(s, s_, s__,1))
print("Erro para y: ", erro(4,s__,s_,0))
print("Erro para z: ", erro(4,s__,s_,1))


h3 = h2/2
print("EXEMPLO RK4 (3):")
s=rk4(h3,0,1,1,0.5)
print(s)
s_=rk4(h3/2,0,1,1,0.5)
print(s_)
s__=rk4(h3/4,0,1,1,0.5)
print(s__)
print("QC para y: ",  quociente_convergencia(s, s_, s__,0))
print("QC para z: ",  quociente_convergencia(s, s_, s__,1))
print("Erro para y: ", erro(4,s__,s_,0))
print("Erro para z: ", erro(4,s__,s_,1))


h4 = h3/2
print("EXEMPLO RK4 (4):")
s=rk4(h4,0,1,1,0.5)
print(s)
s_=rk4(h4/2,0,1,1,0.5)
print(s_)
s__=rk4(h4/4,0,1,1,0.5)
print(s__)
print("QC para y: ",  quociente_convergencia(s, s_, s__,0))
print("QC para z: ",  quociente_convergencia(s, s_, s__,1))
print("Erro para y: ", erro(4,s__,s_,0))
print("Erro para z: ", erro(4,s__,s_,1))