
import numpy as np

def assert_equal(valor_prueba,valor_real):
    print('Hey')
    if isinstance(valor_prueba,float) and abs(valor_prueba-valor_real)<0.01:
        print("ASSERT EQUALS : )")
    elif valor_prueba == valor_real:
        print("ASSERT EQUALS : )")
    else:
        print("FAILED : ( ")

class Cholesky:
    
    def __init__(self,n):#n es la dimension de la matriz cuadrada de coeficientes (numero de ecuacciones e incognitas) [1, ... , n]
        self.n=n
        self.a=np.zeros((n,n+1))
        self.l=np.zeros((n,n))
        self.u=np.zeros((n,n+1))
        self.x=np.ones(n+1)

    def fill_a(self):
        for i in range(self.n):
            for j in range(self.n+1):
                show='A['+str(i+1)+']['+str(j+1)+'] = '
                self.a[i][j]=float(input(show))

    def L1i(self):
        for i in range(self.n):
            self.l[i][0] = self.a[i][0]
    
    def U1j(self):
        for j in range(self.n+1):
            self.u[0][j] = self.a[0][j]/self.a[0][0]

    def Lij(self,i,j):
        sum = 0
        for r in range(j):
            sum += self.l[i][r] * self.u[r][j]
        self.l[i][j] = self.a[i][j] - sum

    def Uij(self,i,j):
        sum = 0
        for r in range(i):
            sum += self.l[i][r] * self.u[r][j]
        self.u[i][j] = (1 / self.l[i][i]) * (self.a[i][j] - sum)

    def find_matrix_L_U(self):
        self.L1i()
        self.U1j()
        for j in range(1,self.n):
            for i in range(j,self.n):
                self.Lij(i,j)
                self.Uij(j,i)
            i = i + 1
            self.Uij(j,i)

    #im a genius of Numpy : ) 
    def find_x(self):
        self.x[self.n-1]=self.u[-1][-1]
        for i in range(self.n-2,-1,-1):
            u_x = self.u[i] * self.x #Se multiplican componente a componente los x (los no hallados son 1)
            self.x[i] = self.u[i][self.n] - u_x[i+1:self.n].sum() #Toma solo en la sumatoria la derecha de la diag princ sin incluirla ni la ultima col de U
        return self.x[:-1]


    def print(self,number):
        print('--------------------------------')
        print('PRINT ',number)
        print("====================")
        print("A")
        print(self.a)
        print("====================")
        print("L")
        print(self.l)
        print("====================")
        print("U")
        print(self.u)

#hacer TEST, pero ya funciona super bien
def test1():
    test1 = Cholesky(3)
    ej1 = np.array([[0.6, 1.6, 0.2, -3.1], [0.0, 0.2, 1.2, 3.6], [2.0, 0.6, 0.0, 1.85]])
    test1.a = ej1
    test1.find_matrix_L_U()
    x_test1 = test1.find_x()
    map(assert_equal,x_test1,np.array([ 1.84555288, -3.06850962,  3.51141827]))
    #assert_equal(x_test1,np.array([ 1.84555288, -3.06850962,  3.51141827]))

def run_all_tests():
    test1()

run_all_tests()

#Cuidar que a[0][0] (El primer valor que se ingresa sea siempre != 0)
#n es la dimension de la matriz cuadrada de coeficientes (numero de ecuacciones) [1, ... , n]

c = Cholesky(3)
c.fill_a()
c.find_matrix_L_U()
c.print(2)
print(c.find_x())