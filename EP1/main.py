import numpy as np

def pedir_ABC(n):
    a=np.empty(n+1)
    b=np.empty(n)
    c=np.empty(n-1)
    for i in range(1,n):
        a[i+1]= int(input("Digite o valor do "+str(i)+"º A: "))
        b[i]= int(input("Digite o valor do "+str(i)+"º B: "))
    for i in range(1,n-1):
        c[i]= int(input("Digite o valor do "+str(i)+"º C: "))
    return(n,a,b,c)
    
def decomposicao_LU(a,b,c,n):
    l = np.empty(n)
    u = np.empty(n)
    u[1]=b[1]

    for i in range(2,n):
        l[i]= a[i]/u[i-1]
        u[i] = b[i]-l[i]*c[i-1]
    return(l,u)

def solucao_LU(l,u,d,c,n):
    y = np.empty(n)
    y[1] = d[1]
    for i in range(2,n):
        y[i]=d[i]-l[i]*y[i-1]
    x= np.empty(n)
    x[n] = y[n]/u[n]
    for i in range(n-1,0,-1):
        x[i]=(y[i]-c[i]*x[i+1])/u[i]
    return(x)

n = int(input("Digite o valor de n que deseja: "))
index = n+1
n,a,b,c = pedir_ABC(index)
l,u = decomposicao_LU(a,b,c,index)
for i in range(1,index):
    d[i] = int(input("Digite os valores de D: "))
x = solucao_LU(l,u,d,c,index)
print(a)
print(b)
print(c)
print(l)
print(u)