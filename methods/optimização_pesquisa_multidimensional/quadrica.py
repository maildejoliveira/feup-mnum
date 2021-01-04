import math as m

#PESQUISA MULTIDIMENSIONAL
#MÉTODO DA QUÁDRICA - pag 196

#Formula de Recorrência: Xn+1=Xn-H^-1*gradiente(x,y)
#Obriga a descobrir a inversa da hessiana (talvez no maxima)

#Passos:
#1. f: y**2-2*x*y-6*y+2*x**2+12+cos(4*x);
#2. grad: [diff(f,x),diff(f,y)];
#3. hessiana: matrix([diff(grad[1],x),diff(grad[1],y)],[diff(grad[2],x),diff(grad[2],y)]);
#4. h_invert : invert(hessiana);

#No entanto podes não recorrer à inversa se souberes a formula de recorrência
#pelo determinante da hessiana

def f(x,y):
    return y**2-2*x*y-6*y+2*x**2+12+m.cos(4*x)

def gradf(x,y):
    return [-2*y -4*m.sin(4*x)+4*x, 2*y-2*x-6]

def hessiana_inversa(x,y):
    return [[(2/(2*(4-16*m.cos(4*x))-4)), (2/(2*(4-16*m.cos(4*x))-4))],[(2/(2*(4-16*m.cos(4*x))-4)),((4-16*m.cos(4*x))/(2*(4-16*m.cos(4*x))-4))]]

def quadrica(xo,yo):
    (x,y)=(xo,yo)
    hx = hessiana_inversa(x, y)[0][0]*gradf(x,y)[0] + hessiana_inversa(x, y)[0][1]*gradf(x,y)[1]
    hy = hessiana_inversa(x, y)[1][0]*gradf(x,y)[0] + hessiana_inversa(x, y)[1][1]*gradf(x,y)[1]
    (xo, yo) = (x-hx, y-hy)
    while(abs(x-xo)>0.0001 and abs(y-yo)>0.0001):
        (x,y)=(xo,yo)
        hx = hessiana_inversa(x, y)[0][0]*gradf(x,y)[0] + hessiana_inversa(x, y)[0][1]*gradf(x,y)[1]
        hy = hessiana_inversa(x, y)[1][0]*gradf(x,y)[0] + hessiana_inversa(x, y)[1][1]*gradf(x,y)[1]
        (xo, yo) = (x-hx, y-hy)
    return xo,yo
    
  
print(quadrica(1,1))
