import numpy as np

class CholeskyModified:
    
    def __init__(self,n):#n es la dimension de la matriz cuadrada de coeficientes
        self.n=n
        self.a=np.zeros((n,n+1))
        self.u=np.zeros((n,n+1))
    
    def fill_a(self):
        for i in range(self.n):
            for j in range(self.n+1):
                show='A['+str(i+1)+']['+str(j+1)+'] = '
                self.a[i][j]=float(input(show))
    
    def U11(self):
        self.u[0][0]=np.sqrt(self.a[0][0])

    def U1j(self):
        for j in range(1,self.n+1):
            self.u[0][j]=self.a[0][j]/self.u[0][0]
    
    def Uii(self,i):
        sum=0
        for r in range(i):
            sum = sum + self.u[r][i] ** 2
        self.u[i][i]= np.sqrt(self.a[i][i]-sum)
    
    def Uij(self,i,j):
        sum = 0
        for r in range(i):
            sum = sum + self.u[r][i] * self.u[r][j]
        self.u[i][j]= (1 / self.u[i][i]) * (self.a[i][j] - sum)

    def find_matrix_U(self):
        self.U11()
        self.U1j()
        for i in range(1,self.n):
            self.Uii(i)
            for j in range(i+1,self.n+1):
                self.Uij(i,j)

'''
cm=CholeskyModified(3)
cm.fill_a()
cm.find_matrix_U()
print(cm.u)
'''

'''
x1 = lambda x2: -2.5 + 0.5 * x2
x2 = lambda x1: 0.8 + 0.6 * x1
print(x1(-0.46))
print(x2(-2.85))
'''

#La matriz de coeficientes debe ser simetrica (que sea igual a su transpuesta)
#Los coeficientes en la diagonal principal de la matriz deben ser positivos 
#n es la dimension de la matriz cuadrada de coeficientes (numero de ecuacciones) [1, ... , n]
cm=CholeskyModified(3)
cm.fill_a()
cm.find_matrix_U()
print(cm.u)
