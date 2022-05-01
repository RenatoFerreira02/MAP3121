import numpy as np
import math
def parametros_ABC(n,ciclica):
   index = n+1
   if(ciclica):
       a=np.empty(index+1)
       b=np.empty(index)
       c=np.empty(index)
       #for i in range(1,index):
           #a[i]= input("Digite o valor do "+str(i)+"º A: ")
           #b[i]= input("Digite o valor do "+str(i)+"º B: ")
       #for i in range(1,index):
           #c[i]= input("Digite o valor do "+str(i)+"º C: ")
       for i in range(1, index):
           a[i] = ((2*i)-1)/(4*i)
           b[i] = 2
           c[i] = 1 - a[i]
   else:
       a=np.empty(index+1)
       b=np.empty(index)
       c=np.empty(index-1)
       for i in range(1,index):
           a[i+1]= input("Digite o valor do "+str(i)+"º A: ")
           b[i]= input("Digite o valor do "+str(i)+"º B: ")
       for i in range(1,n-1):
           c[i]= input("Digite o valor do "+str(i)+"º C: ")
   return(a,b,c)

  
def decomposicao_LU(a,b,c,n):
   index = n+1
   l = np.empty(index)
   u = np.empty(index)
   u[1]=b[1]

   for i in range(2,index):
       l[i]= a[i]/u[i-1]
       u[i] = b[i]-(l[i]*c[i-1])
   return(l,u)

def solucao_LU(l,u,d,c,n):
   index = n+1
   y = np.empty(index)
   y[1] = d[1]
   for i in range(2,index):
       y[i]=d[i]-l[i]*y[i-1]
   x = np.empty(index)
   x[n] = y[n]/u[n]
   for i in range(n-1,0,-1):
       x[i]=(y[i]-c[i]*x[i+1])/u[i]
   return(x)

def solucao_ciclica(l,u,d,c,a,n):
   index = n+1
   v = np.zeros(index)
   v[1]=a[1]
   v[n]=c[n-1]
   y_barra = solucao_LU(l,u,d,c,n-1)
   z_barra = solucao_LU(l,u,v,c,n-1)
   print("y_barra")
   print(y_barra)
   print("z_barra")
   print(z_barra)
   print()
   x=np.empty(index)
   x[n]=(d[n]-c[n]*y_barra[1]-a[n]*y_barra[n-1])/(b[n]-c[n]*z_barra[1]-a[n]*z_barra[n-1])
   for i in range(n-1,0,-1):
       x[i]=y_barra[i]-x[-1]*z_barra[i]
   return x
  
ciclica = bool(input("É uma matriz tridiagonal cíclica?\n0-Não\n1-Sim "))
n = int(input("Digite o valor de n que deseja: "))
a,b,c = parametros_ABC(n,ciclica)
l,u = decomposicao_LU(a,b,c,n)
d = np.empty(n+1)
for i in range(1,n+1):
   #d[i] = input("Digite os valores de D: ")
   argument = (2*math.pi*i*i)
   d[i] = math.cos((argument/n*n))
if(ciclica):
   x = solucao_ciclica(l,u,d,c,a,n)
else:
   x = solucao_LU(l,u,d,c,n)
print()
#print(a)
#print(b)
#print(c)
#print(d)
print("l: ")
print(l)
#print(u)
print("x: ")
print(x)




