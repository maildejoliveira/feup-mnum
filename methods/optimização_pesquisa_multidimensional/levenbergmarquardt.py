#PESQUISA MULTIDIMENSIONAL
#MÉTODO De Levenberg-Marquardt - pag 197

#Formula de Recorrência: Xn+1=Xn-h(LM)
# h(LM) = hessiana^-1*gradf + lambda*gradf
#Obriga a descobrir a inversa da hessiana (talvez no maxima)

#Passos:
#1. f: y**2-2*x*y-6*y+2*x**2+12+cos(4*x);
#2. grad: [diff(f,x),diff(f,y)];
#3. hessiana: matrix([diff(grad[1],x),diff(grad[1],y)],[diff(grad[2],x),diff(grad[2],y)]);
#4. h_invert : invert(hessiana);

#No entanto podes não recorrer à inversa se souberes a formula de recorrência
#pelo determinante da hessiana

def f(x,y):
    return (x+1)**2+(y-4)**2

def gradf(x,y):
    return [2*(x+1),2*(y-4)]

def hessiana_inversa(x,y):
    return [[0.5,0],[0,0.5]]

def lm(xo,yo, l):
    (x,y)=(xo,yo)
    hx = hessiana_inversa(x, y)[0][0]*gradf(x,y)[0] + hessiana_inversa(x, y)[0][1]*gradf(x, y)[1] + l*gradf(x,y)[0]
    hy = hessiana_inversa(x, y)[1][0]*gradf(x,y)[0] + hessiana_inversa(x, y)[1][1]*gradf(x, y)[1] + l*gradf(x,y)[1]
    (xo,yo)=(x-hx,y-hy)
    while(abs(x-xo)>0.0001 and abs(y-yo)>0.0001):
        (x,y)=(xo,yo)
        hx = hessiana_inversa(x, y)[0][0]*gradf(x,y)[0] + hessiana_inversa(x, y)[0][1]*gradf(x, y)[1] + l*gradf(x,y)[0]
        hy = hessiana_inversa(x, y)[1][0]*gradf(x,y)[0] + hessiana_inversa(x, y)[1][1]*gradf(x, y)[1] + l*gradf(x,y)[1]
        (xo,yo)=(x-hx,y-hy)     
    return xo,yo

print(lm(1,1,0.05))
