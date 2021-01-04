import math

#PESQUISA DE ZEROS REAIS DE UM SISTEMA NÃO LINEAR
#RESOLUÇÃO ITERATIVA DE SISTEMAS DE EQUAÇÕES
#cap2 (2.6)
#metodos para descobrir zeros de um sistema não linear
#metodos não intervalares, maior risco de afastar do zero


#Método de Newton (ou da Tangente) - pag 65 (equação do metodo pag 69)
#tem limitaçoes
#Critério de Convergência obrigatorio: det(jacobiana)!=0 no guess
#JACOBIANO:
#       f'1,x   f'1,y
#       f'2,x   f'2,y
#isto é as f1_x()*f2_y()-f2_x()*f1_y()!=0
#Fórmula de Recorrência:x(n+1)=x-(f1(x,y)*f2_y(x,y)-f2(x,y)*f1_y(x,y))/(f1_x(x,y)*f2_y(x,y)-f2_x(x,y)*f1_y(x,y))
#                       y(n+1)=y-(f2(x,y)*f1_x(x,y)-f1(x,y)*f2_x(x,y))/(f1_x(x,y)*f2_y(x,y)-f2_x(x,y)*f1_y(x,y))
#Critério de Paragem: |x(n+1)-x(n)|<=10^-4 (igual para y)
#Escolha do GUESS: guess deve ser proximo da raiz
#se com o guess escolhido não convergir esolher outro

#1.ver função no máxima
#2.quantas raízes tem? 
#3.escolha um guess para cada raiz (neste ex guessx=4, guessy=4, para testar)
#4.aplicar o metodo com um erro escolhido
#5.verificar se converge, se não convergir escolher outro guess
#6.análise crítica dos resultados: rapidez, precisão e convergência

#defenir função f1 e suas derivadas parciais 
def f1(x,y):
    return 2*x**2-x*y-5*x+1

#defenir função f2 e suas derivadas parciais
def f2(x,y):
    return x+3*math.log(x)-y**2

def f1_x(x,y):
    return -y+4*x-5

def f1_y(x,y):
    return -x

def f2_x(x,y):
    return 3/x + 1

def f2_y(x,y):
    return -2*y

def newton_nl(guessx,guessy):
    x=-1
    y=-1
    counter=0
    while(abs(x-guessx)>0.000001 or abs(y-guessy)>0.000001):
        x=guessx
        y=guessy
        counter +=1
        guessx=x-(f1(x,y)*f2_y(x,y)-f2(x,y)*f1_y(x,y))/(f1_x(x,y)*f2_y(x,y)-f2_x(x,y)*f1_y(x,y))
        guessy=y-(f2(x,y)*f1_x(x,y)-f1(x,y)*f2_x(x,y))/(f1_x(x,y)*f2_y(x,y)-f2_x(x,y)*f1_y(x,y))
    print(counter)
    print(x)
    print(y)
    return 

print("Newton:")
print(newton_nl(4,4))



    
    
    
    
    
    