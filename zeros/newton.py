import math

#PESQUISA DE ZEROS REAIS DE UMA FUNÇÃO REAL
#cap2
#metodos para descobrir zeros de uma função
#metodos não intervalares, maior risco de afastar do zero


#Método de Newton (ou da Tangente) - pag 58
#tem limitaçoes
#obrigatoriedade de verificar em cada iteração se a derivada é diferente de 0
#Fórmula de Recorrência: x(n+1)=x(n)-f(x(n))/f_(x(n))
#Critério de Paragem: |x(n+1)-x(n)|<=10^-4
#Escolha do GUESS: guess deve ser proximo da raiz
#se com o guess escolhido não convergir esolher outro

#1.ver função no máxima
#2.quantas raízes tem?
#3.escolha um guess para cada raiz
#4.aplicar o metodo com um erro escolhido
#5. verificar se converge, se não convergir escolher outro guess
#6.análise crítica dos resultados: rapidez, precisão e convergência

#define a tua função
def f(x):
    return x-2*math.log(x)-5
    #proj: return x*math.exp(-x*1.3)-0.347*math.exp(-0.347*1.3)

#descobre a derivada (por exemplo no maxima)
def f_(x):
    return 1-2/x

def newton(guess):
    x=0
    counter=0
    while(abs(guess-x)>0.000001):
        x=guess
        counter+=1
        if(f_(x)==0):
            print("error")
            return 0
        guess = x-f(x)/f_(x)
    print(counter)
    return x

print(newton(0.1))
