import numpy as np

def pedir_NABC():
    n = int(input("Digite o valor de n que deseja"))
    a=np.empty(n)
    b=np.empty(n)
    c=np.empty(n)
    for i in range(1,n):
        a[i]= int(input("Digite o valor do"+str(i)+"º A"))
        b[i]= int(input("Digite o valor do"+str(i)+"º B"))
        c[i]= int(input("Digite o valor do"+str(i)+"º C"))
    return(n,a,b,c)
    
def decomposicao_LU(a,b,c):
    l = np.empty(n)
    u = np.empty(n)
    u[1]=b[1]

    for i in range(2,n):
        l[i]= a[i]/u[i-1]
        u[i] = b[i]-l[i]*c[i-1]
    return(l,u)

def solucao_LU(l,u,d,c):
    y = np.empty(n)
    y[1] = d[1];
    for i in range(2,n):
        y[i]=d[i]-l[i]*y[i-1]
    x[n] = y[n]/u[n]
    for i in range(n-1,0,-1):
        x[i]=(y[i]-c[i]*x[i+1])/u[i]
    return(x)

n,a,b,c = pedir_NABC()
print(n,a,b,c)