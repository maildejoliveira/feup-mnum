import math

#Método de Picard Peano - pag 61
#como não sabemos f(x)=0 então podemos tentar transformar a função em x=g(x)
#NOTA: função g(x) escolhida pode não servir para todos os zeros da funçao f
#Critério de Paragem: |x(n+1)-x(n)|<=10^-4
#Escolha do GUESS: guess deve ser proximo da raiz
#se com o guess escolhido não convergir esolher outro

#1.ver função no máxima
#2.quantas raízes tem?
#3.escolha um guess para cada raiz
#4.descobrir função g(x) tal que x=g(x)
#5.calcular a derivada de g(x) para verificar convergência (não precisas no metodo)
#6.verificar a convergência de g(x), isto é |g_(guess)|<1
#7.se a condição se verificar, converge e serve para este zero
#8.aplicar o metodo com um erro escolhido
#9.verificar se converge, se não convergir escolher outro guess
#10.análise crítica dos resultados: rapidez, precisão e convergência

#define a tua função auxiliar g
def g(x):
    #exemplo escolhido havia outras para outros zeros
    return 2*math.log(x)+5

def picardpeano(guess):
    x=0
    counter=0
    while(abs(guess-x)>0.000001):
        x=guess
        counter+=1
        guess = g(x)
    print(counter)
    return x

print(newton(0.1))
print(picardpeano(9))
print("sao duas raizes diferentes")