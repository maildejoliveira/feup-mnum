#OPTIMIZAÇÃO MULTIDIMENSIONAL / PESQUISA MULTIDIMENSIONAL

#MÉTODO DO GRADIENTE - pag 184
#pag 192

#Concelho - plot3d() no máxima

#Formula de Recorrência: (ponto seguinte) Xn+1 = Xn - h*gradiente

#h é um multiplicador que controla o passo e é decidido pelo utilizador

#Critério de paragem: |x1-x2| <= erro and |y1-y2| <= erro

def f(x,y):
    return 2**2-2*x*y-6*y+2*x**2+12

def gradiente(x,y):
    return -2*y +4*x, 2*y-2*x-6

def op_multi(h,x1,y1):
    (x2,y2)=(-1,-1)
    counter =0
    while(abs(x2-x1)>0.01 or abs(y2-y1)>=0.01):
        if(counter==0): (x2,y2)=(x1,y1)
        counter +=1
        (x1,y1)=(x2,y2)
        (x2,y2)=gradiente(x1,y1)
        (x2,y2)=(x2*h,y2*h)
        (x2,y2)=(x1-x2,y1-y2)
        if(f(x2,y2)<f(x1,y1)):
            h*=2
        else:
            h/=2
    return x1,y2
        
print(op_multi(1.0,0,0))
