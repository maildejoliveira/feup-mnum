#CHOLESLY

#Sistema: A.x = b
#procuremos representar A na forma do produto de uma matriz triangular inferior, B, 
#por uma matriz triangular superior de diagonal unitária, C: A = B.C

#é imediato verificar, procedendo a multiplicação:
#1. bi1 = ai1
#2. bi j = aij − ∑(k=1->j-1) bik.ckj (se i ≥ j)
#3. c1i =a1i/b11
#4. ci j = (aij − ∑(k=1->i-1) bik.ckj)/bii (se i < j)

#Então o vector procurado, x, pode ser calculado a partir dos sistemas encadeados
#   B.y = b
#   C.x = y
#sistema que é facilmente resolúvel por ter matrizes triangulares:
#1. y1 = a1.n+1
#2. yi = (a1.n+1 −∑(k=1->i−1) bik.yk)/bii
#3. xn = yn
#4. xi = yi − ∑(k=i+1->n) bik.yk

def cholesky(A,b):
    print("A: ",A)
    print("b: ", b)
    
    #inicializar 1ªcoluna de B
    #bi1 = ai1
    B=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(A)):
        B[i][0]=A[i][0]
        
    #inicializar 1ªlinha de C
    #c1i =a1i/b11
    C=[[1,0,0],[0,1,0],[0,0,1]]
    for i in range(len(A)):
        C[0][i]=A[0][i]/B[0][0]
        
    #construir B
    sum = 0
    for i in range(len(A)):
        for j in range(len(A)):
            sum=0
            if(i>=j):
                k=0
                while(k<=j-1):
                    sum += B[i][k]*C[k][j]
                    k+=1
                #bij = aij − ∑(k=1->j-1) bik.ckj (se i ≥ j)
                B[i][j]=A[i][j]-sum 
            elif(i<j):
                k=0
                while(k<=i-1):
                    sum += B[i][k]*C[k][j]
                    k+=1
                #cij = (aij − ∑(k=1->i-1) bik.ckj)/bii (se i < j)
                C[i][j]=(A[i][j]-sum)/B[i][i]
            
    print("B: ", B)
    print("C: ", C)
    
    #find Y
    #B.y = b
    y=[0,0,0]
    for i in range (len(y)): #i -> linha 
        sum =0
        sum += b[i]
        k=0
        while(k<i):
            sum -= B[i][k]*y[k]
            k+=1
        sum /= B[i][i]
        y[i]= sum
    print("Y: ",y)
    
    #find x
    #C.x = y    
    x=[0,0,0]
    for i in reversed(range(0,3)): #i -> linha 
        sum =0
        sum += y[i]
        k=2
        while(k>i and k<=2):
            sum -= C[i][k]*x[k]
            k-=1
        sum /= C[i][i]
        x[i]= sum
    print("X: ",x)
    
    return 
    
    

print(cholesky([[1,1,1],[3,-1,2],[2,0,2]],[8,-1,5]))
        
    
    
    


