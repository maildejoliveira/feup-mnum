import math as m
#EXAME 2014/2015

#Pergunta 1 - Euler
#dT/dt = -0.25(T-Ta)

def temp(t,T):
    return -0.25*(T-37)

def euler(to,To,tf,h):
    counter = 0
    while(abs(to-tf)>0.000 and counter<3):
        print(to,To)
        t_ = temp(to,To)
        to += h
        To += h*t_
        counter += 1
    return to,tf

print(euler(5,3,1,0.4))
print("RESPOSTA P1:", 9.460000)

#Pergunta 2 - ESTUDAR!!!!!!!!!!!!, Erros

#Pergunta 3 - Máxima, Gauss

#Passos:
#1. A: matrix([1,1/2,1/3],[1/2,1/3,1/4],[1/3,1/4,1/5]);
#2. B: matrix([-1],[1],[1]);
#3. AB: addcol(A,B);
#4. echelon(AB); - aqui obtemos a matrix triangular superior para preencher a)
print("Resposta P3a):",[1,0.5,0.3333333,-1.0],[0,1,1.00000,18.00000],[0,0,1,-30.00000])

#5. invert(A).B; - resultados 
print("Resposta P3b):", [-15],[48],[-30])

#6. DA:zeromatrix(3,3)+da;
#7. DB:zeromatrix(3,1)+db;
#8. X:invert(A).B;
#9. BP:DB-DA.X;
#10. AP:addcol(A,BP);
#11. AP:echelon(AP); - substituindo os valores da= 0.05 e db = 0.05
#12. subst([da=0.05,db=0.05],AP); - obtemos matriz triangular superior
print("Resposta P3c)1:",[1,0.5,0.3333333,-0.10],[0,1,1.00000,-0.600000],[0,0,1,-3.00000])

#13. invert(A).BP;
#14. subst([da=0.05,db=0.05],%);
print("Resposta P3c)2:", [-0.3],[2.4],[-3.0])
print("Resposta P3d): x3" ,[-3.0])


#Pergunta 4 - Picard-Peanoº
print("Resposta P4")

#f(x)= exp(x)-4*x**2
#Intervalos: 
    #x1 [-1,0]
    #x2 [0,1]
    #x3 [4,5]

#1. g1: 1/2*sqrt(exp(x));
#   g1_: diff(g1,x);
print("Resposta P4.1a) x1 e x2")

#2. g2: exp(x)/(4*x);
#   g2_:diff(g2,x);
#(nao funciona para zeros)
print("Resposta P4.1b) nenhuma")

#3. g3: -1/2*sqrt(exp(x));
#   g3_: diff(g3,x);
print("Resposta P4.1c) x1 e x2")

#Fórmula de Recorrência
def recorrencia(x):
    return 2*m.log(2*x)

def picardpeano(guess):
    counter =0
    x = 0
    while(abs(guess-x)>0.00001):
        x = guess
        if(counter < 2):
            print("Resposta P4.2",guess)
        guess = recorrencia(x)
        counter += 1
    return guess
        
print(picardpeano(1.1))
#NOTA: resíduo ao fim da primeira iteração é quanto andou o guess 
print("Resposta P4.3", 1.57691-1.1)

#Pergunta 5 - Trapézios e Simpson

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

print("Resposta P5 h:", 0.125,0.125)
print("Resposta P5 h'':", 0.125/2,0.125/2)
print("Resposta P5 h''':", 0.125/4,0.125/4)
print("Resposta P5 L1: ",trapezios(0,1,0.125),simpson(0,1,0.125))
print("Resposta P5 L2: ",trapezios(0,1,0.125/2),simpson(0,1,0.125/2))
print("Resposta P5 L3: ",trapezios(0,1,0.125/4),simpson(0,1,0.125/4))

def quociente(s,s_,s__):
    return (s_-s)/(s__-s_)

def erro(s_,s__,ordem):
    return (s__-s_)/(2**ordem-1)

print("Resposta P5 QC: ",quociente(trapezios(0,1,0.125), trapezios(0,1,0.125/2),trapezios(0,1,0.125/4)), quociente(simpson(0,1,0.125), simpson(0,1,0.125/2),simpson(0,1,0.125/4)))
print("Resposta P5 ER: ",erro(trapezios(0,1,0.125/2),trapezios(0,1,0.125/4),2), erro(simpson(0,1,0.125/2),simpson(0,1,0.125/4),4))

#Pergunta 6 - ESTUDAR!!!!!!,Optimização

#Pergunta 7 - Bisseção

def ff(x):
    return x**3-10*m.sin(x)+2.8

def bissec(xo,xf):
    counter = 0
    while(abs(xo-xf)>0.00001):
        m = (xo+xf)/2
        if(counter == 2):
            print("Resposta P7: ", xf)
        if(ff(xo)*ff(m)<0):
            xf = m
        else: 
            xo = m
        counter += 1
    return xo
            
            
print(bissec(1.5,4.2))
        


        
    


        

        

