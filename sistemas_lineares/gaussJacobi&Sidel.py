#SISTEMAS DE EQUAÇÕES LINEARES
#cap3
#metodos para resolução de equações lineares
#METODOS ITERATIVOS - pag 112


#Método de Gauss Jacobi - pag 113
#tem limitaçoes

#Critério de Convergência: verificar se a matriz é diagonalmente dominante, isto é
#   em cada linha elemento que pertence à diagonal da matriz
#   o seu coeficiente tem que ser maior que a soma dos coeficientes que não pertencem a diagonal

#Fórmula de Recorrência: 
# exemplo:
#   3x+y+2z=7           - x=(7-y-z)/3
#   x+4y+2z=4           - y=(4-x-2z)/4
#   2x+5z=5             - z=(5-2x)/5
    
    
#Critério de Paragem: |x(n+1)-x(n)|<=10^-4 (para as outras variáveis também)

#Formulas de Recorrência

def x_recorr(y,z):
    return (7-y-z)/3

def y_recorr(x,z):
    return (4-x-2*z)/4

def z_recorr(x,y):
    return (5-2*y)/5


def gaussJacobi(xo,yo,zo):
    x=-1
    y=-1
    z=-1
    counter=0
    while(abs(x-xo)>0.000001 or abs(y-yo)>0.000001 or abs(z-zo)>0.000001):
        x=xo
        y=yo
        z=zo
        counter +=1
        xo = x_recorr(y,z)
        yo = y_recorr(x,z)
        zo = z_recorr(x,y)
    print(counter)
    print(x)
    print(y)
    print(z)
    return 0


#Método de Gauss Sidel - pag 113
#tem limitaçoes

#Critério de Convergência: verificar se a matriz é diagonalmente dominante, isto é
#   em cada linha elemento que pertence à diagonal da matriz
#   o seu coeficiente tem que ser maior que a soma dos coeficientes que não pertencem a diagonal

#Fórmula de Recorrência: 
# exemplo:
#   3x+y+2z=7           - x=(7-y-z)/3
#   x+4y+2z=4           - y=(4-x-2z)/4
#   2x+5z=5             - z=(5-2x)/5

#NOTA: formulas de recorrência são iguais as de Jacobi no entanto,
#no código são aplicadas aos valores antigos de xo,yo,zo e em jacobi a x,y,x
       
#Critério de Paragem: |x(n+1)-x(n)|<=10^-4 (para as outras variáveis também)

def gaussSidel(xo,yo,zo):
    x=-1
    y=-1
    z=-1
    counter=0
    while(abs(x-xo)>0.000001 or abs(y-yo)>0.000001 or abs(z-zo)>0.000001):
        x=xo
        y=yo
        z=zo
        xo = x_recorr(yo,zo)
        yo = y_recorr(xo,zo)
        zo = z_recorr(xo,yo)
        counter +=1
    print(counter)
    print(x)
    print(y)
    print(z)
    return 0

print("EXEMPLO:")
print(gaussJacobi(0, 0, 0))
print(gaussSidel(0, 0, 0))



    
