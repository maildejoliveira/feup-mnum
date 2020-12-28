import math 

#PESQUISA DE ZEROS REAIS DE UM SISTEMA NÃO LINEAR
#RESOLUÇÃO ITERATIVA DE SISTEMAS DE EQUAÇÕES
#cap2 (2.6)
#metodos para descobrir zeros de um sistema não linear
#metodos não intervalares, maior risco de afastar do zero

#Método de PicardPeano - pag 67 ()
#tem limitaçoes
#Critério de Convergência obrigatorio: |g1_x(guesses)|<1 &&  |g1_y(guesses)|<1  
# && |g2_x(guesses)|<1 &&  |g2_y(guesses)|<1 
#Fórmula de Recorrência:x(n+1)=g1(x,y)
#                       y(n+1)=g2(x,y)
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

#defenir função g1 x=g1(x,y) (após verificação do critério de convergência)
def g1(x,y):
    return math.sqrt((x*y+5*x-1)/2)

#defenir função g2 y=g2(x,y) (após verificação do critério de convergência)
def g2(x,y):
    return math.sqrt(x+3*math.log(x))

def picardpeano_nl(guessx,guessy):
    x=-1
    y=-1
    counter=0
    while(abs(x-guessx)>0.000001 or abs(y-guessy)>0.000001):
        x=guessx
        y=guessy
        counter +=1
        guessx=g1(x,y)
        guessy=g2(x,y)
    print(counter)
    print(x)
    print(y)
    return 

print("PP:",picardpeano_nl(4,4))

#outro método em aula unica variação para picarpeano é na atualização:
#x(n+1)=g1(x,y)
#y(n+1)=g2(guessx,y)
def gausssidel_nl(guessx,guessy):
    x=-1
    y=-1
    counter=0
    while(abs(x-guessx)>0.000001 or abs(y-guessy)>0.000001):
        x=guessx
        y=guessy
        counter +=1
        guessx=g1(x,y)
        guessy=g2(guessx,y)
    print(counter)
    print(x)
    print(y)
    return

print("GaussSidel: ",gausssidel_nl(4, 4))