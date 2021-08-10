#m = numero de ecuaciones (filas de la matriz)
import numpy as np
import sympy
from sympy import *

def error(x1,x0):
    if x1 == 0:
        x1 = 1
    return abs((x1-x0)/x1)*100

class GaussSeidel:

    def __init__(self,m):
        self.ecuas = []
        self.m = m #numero de ecuaciones
        self.xs = []
        self.hist = []

    def fill_ecuations(self,ecuas=False):
        i = 0
        if isinstance(ecuas,bool):
            while i < self.m:
                expr = input()
                self.ecuas.append(sympify(expr))
                i = i + 1
        else:
            for expr in ecuas:
                self.ecuas.append(sympify(expr))

    def despejando_ecuaciones(self, xs):
        i = 0
        for x in xs:
            self.xs.append( Symbol(xs[i]) )
            i = i + 1
        i = 0
        print('------------------------------')
        print('Despejando')
        for j in self.ecuas:
            self.ecuas[i] = sympy.solve(self.ecuas[i], self.xs[i])
            print(self.xs[i], ' = ', self.ecuas[i])
            i = i + 1
        print('------------------------------')
        return self.ecuas, self.xs


    def gauss_seidel(self,init_val, desp_equ, eps = 0.01, max_n=20):
        ans = init_val
        self.hist.append(init_val.copy())
        n = 0  # iterations
        new_desp_equ = []
        for i in desp_equ:
            new_desp_equ.append(i.copy())
        while n < max_n:
            for i in range(len(desp_equ)):
                new_desp_equ[i][0] = desp_equ[i][0]
                for j in range(len(vari)):
                    if i != j:
                        new_desp_equ[i][0] = new_desp_equ[i][0].subs(vari[j], ans[j])
                ans[i] = float(new_desp_equ[i][0])
            self.hist.append(ans.copy())
            n = n + 1
            errors = np.zeros(len(vari))
            for i in range(len(vari)):
                errors[i] = error(self.hist[n][i],self.hist[n-1][i])
            total_err = errors.sum()/self.m
            if total_err < eps:
                break
        return self.hist

    def show_hist(self):
        for step in self.hist:
            print(list(map(lambda x: round(x,4),step)))

se = GaussSeidel(3)
vari = ['x','y','z']
ecuas = ['x+y+z-500',
         'x+y-60-z',
         '1.06*x+1.12*y+1.3*z-592.4']
se.fill_ecuations(ecuas=ecuas)
ecuas, _ = se.despejando_ecuaciones(vari)
hist = se.gauss_seidel([0,160,180],ecuas)
se.show_hist()

'''
se = GaussSeidel(3)
vari = ['x','y','z']
ecuas = ['6*x+y-z-14',
         '4*x+2*y-z-13',
         'x+2*y+4*z-12']
se.fill_ecuations(ecuas=ecuas)
ecuas, _ = se.despejando_ecuaciones(vari)
hist = se.gauss_seidel([0,0,0],ecuas)
se.show_hist()

se = GaussSeidel(2)
vari = ['x1','x2']
ecuas = ['-2*x1+x2-5',
         '3*x1-5*x2+4']
se.fill_ecuations(ecuas=ecuas)
ecuas, _ = se.despejando_ecuaciones(vari)
hist = se.gauss_seidel([0,0],ecuas)
se.show_hist()

se = GaussSeidel(3)
vari = ['x','y','z']
ecuas = ['0.3*x+0.2*y-0.3*z',
         '-0.3*x+0.1*y+0.1*z',
         '-0.5*x-0.5*y+z-350']
se.fill_ecuations(ecuas=ecuas)
ecuas, _ = se.despejando_ecuaciones(vari)
hist = se.gauss_seidel([400,580,880],ecuas)
se.show_hist()

se = GaussSeidel(2)
vari = ['x','y']
ecuas = ['2*x+3*y+2','-x+4*y+8']
se.fill_ecuations(ecuas=ecuas)
ecuas, _ = se.despejando_ecuaciones(vari)
hist = se.gauss_seidel([0,0],ecuas)
se.show_hist()

se = GaussSeidel(2)
vari = ['x1','x2']
ecuas = ['3*x1+x2-11','2*x1+5*x2-16']
se.fill_ecuations(ecuas=ecuas)
ecuas, _ = se.despejando_ecuaciones(vari)
hist = se.gauss_seidel([0,0],ecuas)
se.show_hist()

#CASO RARO PORQUE NO DA AL REVES
se = GaussSeidel(2)
vari = ['x1','x2']
ecuas = ['2*x1+5*x2-16','3*x1+x2-11']
se.fill_ecuations(ecuas=ecuas)
ecuas, _ = se.despejando_ecuaciones(vari)
hist = se.gauss_seidel([0,0],ecuas)
se.show_hist()
'''
'''
ecuas = []
m = int(input())
i=0
while i < m:
    expr = input()
    ecuas.append(sympify(expr))
    i = i + 1

def despejando_ecuaciones(ecua,xs):
    i = 0
    for x in xs:
        xs[i] = Symbol(xs[i])
        i = i + 1
    i = 0
    print('Despejando ___________________')
    for j in ecua:
        ecua[i] = sympy.solve(ecua[i],xs[i])
        print(xs[i],' = ',ecua[i])
        i = i + 1
    print('------------------------------')
    return ecua,xs

def gauss_seidel(init_val,desp_equ,vari,eps,max_n = 20):
    ans = init_val
    hist = []
    hist.append(init_val.copy())
    n = 0#iterations
    new_desp_equ = []
    #si se hace copy de una lista, no se hace una copia del valor de cada elemento
    #sigue manejandose las referencias
    #por eso ...
    for i in desp_equ:
        new_desp_equ.append(i.copy())
    while n < max_n:
        for i in range(len(desp_equ)):
            new_desp_equ[i][0] = desp_equ[i][0]
            for j in range(len(vari)):
                if i != j:
                    new_desp_equ[i][0] = new_desp_equ[i][0].subs(vari[j],ans[j])
            ans[i] = float(new_desp_equ[i][0])
        hist.append(ans.copy())
        n = n + 1
        #print(type(float(ans[i][0])))
        if abs(hist[n][0]- hist[n-1][0])< eps:
            break
    return hist


vari = ['x1','x2']
ecuas,vari = despejando_ecuaciones(ecuas,vari)
init_val = [0,0]
hist = gauss_seidel(init_val,ecuas,vari,0.001)
for i in hist:
    print(i)
    
vari = ['x1','x2']
ecuas,vari = despejando_ecuaciones(ecuas,vari)
init_val = [0,0]
hist = gauss_seidel(init_val,ecuas,vari,0.001)
for i in hist:
    print(i)
'''
#TODO
#generalizar los nombres de las variables, valores iniciales
#probar con otros casos