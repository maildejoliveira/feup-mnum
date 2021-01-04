def x_recorr(x,y,z,w):
    return (25-0.5*y-3*z-0.25*w)/6

def y_recorr(x,y,z,w):
    return (10-1.2*x-0.25*z-0.2*w)/3

def z_recorr(x,y,z,w):
    return (7+x-0.25*y-2*w)/4

def w_recorr(x,y,z,w):
    return (-12-2*x-4*y-z)/8


def gaussidel(xo,yo,zo,wo):
    x = x_recorr(xo,yo,zo,wo)
    y = y_recorr(xo,yo,zo,wo)
    z = z_recorr(xo,yo,zo,wo)
    w = w_recorr(xo,yo,zo,wo)
    return x,y,z,w

print(gaussidel(2.12687,2.39858,3.99517,-3.73040))


def y_(t,y,z):
    return z

def z_(t,y,z):
    return 2+t**2+t*z


def euler(to,yo,zo,h):
    n = 0
    while(n<3):
        print(to,yo,zo)
        t = to
        y = yo
        z = zo
        to += h
        yo += h*y_(t,y,z)
        zo += h*z_(t,y,z)     
        n+= 1
    return


print(euler(1,1,0,0.25))


def rk4(to,yo,zo,h):
    n = 0
    while(n<3):
        print(to,yo,zo)
        t = to
        y = yo
        z = zo
        y1 = h*y_(t,y,z)
        z1 = h*z_(t,y,z)
        y2 = h*y_(t+h/2,y+y1/2,z+z1/2)
        z2 = h*z_(t+h/2,y+y1/2,z+z1/2)
        y3 = h*y_(t+h/2,y+y2/2,z+z2/2)
        z3 = h*z_(t+h/2,y+y2/2,z+z2/2)
        y4 = h*y_(t+h,y+y3,z+z3)
        z4 = h*z_(t+h,y+y3,z+z3)
        yy = y1/6 + y2/3 + y3/3 + y4/6
        zz = z1/6 + z2/3 + z3/3 + z4/6
        to += h
        yo += yy
        zo += zz    
        n+= 1
    return

print(rk4(1,1,0,0.25))
    
    