#Teste 2019.2

#p1 maxima
#p2 maxima

#p3

def x_recorr(x,y,z,w):
    return (2.5-0.5*y-3*z-0.25*w)/6

def y_recorr(x,y,z,w):
    return (3.8-1.2*x-0.25*z-0.2*w)/3

def z_recorr(x,y,z,w):
    return (10+x-0.25*y-2*w)/4

def w_recorr(x,y,z,w):
    return (7-2*x-4*y-z)/8


def gaussidel(xo,yo,zo,wo):
    x= xo
    y=yo
    z=zo
    w=wo
    x = x_recorr(x,y,z,w)
    y = y_recorr(x,y,z,w)
    z = z_recorr(x,y,z,w)
    w = w_recorr(x,y,z,w)
    return x,y,z,w

print(gaussidel(-0.81959,1.40167,2.15095,0.11019))

#v(1)=0.1

def vfunc(u,v):
    return u*(u/2+1)*v**3+(u+5/2)*v**2

def euler(uo,vo,uf,h):
    u = uo
    v = vo
    while(abs(uo-uf)>0.0001):
        uo = u
        vo = v
        u += h
        v += h*vfunc(uo,vo)
    return vo

print("h=", 0.08, euler(1.0,0.1,1.8,0.08))
print("h=", 0.08/2, euler(1.0,0.1,1.8,0.08/2))
print("h=", 0.08/4, euler(1.0,0.1,1.8,0.08/4))



def qc(s,s_,s__):
    return (s_-s)/(s__-s_)

def erro(s_,s__, o):
    return (s_-s__)/(2**o-1)


print(qc(euler(1.0,0.1,1.8,0.08),euler(1.0,0.1,1.8,0.08/2),euler(1.0,0.1,1.8,0.08/4)))
print(erro(euler(1.0,0.1,1.8,0.08/2),euler(1.0,0.1,1.8,0.08/4),1))


def rk4(uo,vo,uf,h):
    u = uo
    v = vo
    while(abs(uo-uf)>0.0001):
        uo = u
        vo = v
        v1 = h*vfunc(uo,vo)
        v2 = h*vfunc(uo+h/2,vo+v1/2)
        v3 = h*vfunc(uo+h/2,vo+v2/2)
        v4 = h*vfunc(uo+h,vo+v3)
        vinc = v1/6 + v2/3 + v3/3 + v4/6
        u += h
        v += vinc
    return vo


print("h=", 0.16, rk4(1.0,0.1,2.6,0.16))
print("h=", 0.16/2, rk4(1.0,0.1,2.6,0.16/2))
print("h=", 0.16/4, rk4(1.0,0.1,2.6,0.16/4))

print(qc(rk4(1.0,0.1,1.8,0.08),rk4(1.0,0.1,1.8,0.08/2),rk4(1.0,0.1,1.8,0.08/4)))
print(erro(rk4(1.0,0.1,1.8,0.08/2),rk4(1.0,0.1,1.8,0.08/4),1))

def f(t,y,z):
    return z

def g(t,y,z):
    return 0.5 + t**2 + t*z

def euler(to,yo,zo,niter,h):
    t = to
    y = yo
    z = zo
    n = 0
    while(n < niter):
        print(n,t,y)
        to = t
        yo = y
        zo = z
        t += h
        y += h*f(t,y,z)
        z += h*g(t,y,z) 
        n += 1
    return 


print(euler(0,0,1,3,0.25))

def rk4(to,yo,zo,niter,h):
    t = to
    y = yo
    z = zo
    n = 0
    while(n < niter):
        print(n,t,y)
        to = t
        yo = y
        zo = z
        y1 = h*f(to,yo,zo)
        z1 = h*g(to,yo,zo)
        y2 = h*f(to+h/2,yo+y1/2, zo+z1/2)
        z2 = h*g(to+h/2,yo+y1/2, zo+z1/2)
        y3 = h*f(to+h/2,yo+y2/2, zo+z2/2)
        z3 = h*g(to+h/2,yo+y2/2, zo+z2/2)
        y4 = h*f(to+h,yo+y3,zo+z3)
        z4 = h*g(to+h,yo+y3,zo+z3)
        yinc = y1/6 + y2/3 + y3/3 + y4/6
        zinc = z1/6 + z2/3 + z3/3 + z4/6
        t += h
        y += yinc
        z += zinc
        n += 1
    return 

print(rk4(0,0,1,3,0.25))

def ff(t,y,z):
    return z

def gg(t,y,z):
    return 1 + t**2 + t*z

def euler2(to,yo,zo,niter,h):
    t = to
    y = yo
    z = zo
    n = 0
    while(n < niter):
        print(n,t,y)
        to = t
        yo = y
        zo = z
        t += h
        y += h*ff(t,y,z)
        z += h*gg(t,y,z) 
        n += 1
    return 


print(euler2(0,1,2,3,0.5))

def rk42(to,yo,zo,niter,h):
    t = to
    y = yo
    z = zo
    n = 0
    while(n < niter):
        print(n,t,y)
        to = t
        yo = y
        zo = z
        y1 = h*ff(to,yo,zo)
        z1 = h*gg(to,yo,zo)
        y2 = h*ff(to+h/2,yo+y1/2, zo+z1/2)
        z2 = h*gg(to+h/2,yo+y1/2, zo+z1/2)
        y3 = h*ff(to+h/2,yo+y2/2, zo+z2/2)
        z3 = h*gg(to+h/2,yo+y2/2, zo+z2/2)
        y4 = h*ff(to+h,yo+y3,zo+z3)
        z4 = h*gg(to+h,yo+y3,zo+z3)
        yinc = y1/6 + y2/3 + y3/3 + y4/6
        zinc = z1/6 + z2/3 + z3/3 + z4/6
        t += h
        y += yinc
        z += zinc
        n += 1
    return 

print(rk42(0,1,2,3,0.5))


