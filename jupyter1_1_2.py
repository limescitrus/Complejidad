import numpy as np
import matplotlib.pyplot as plt
import math
###*********** Este programa funciona para mapeos de cualquier dimensión entera,sólo hay que tener cuidado que la
#************* condición inicial que le metamos sea adecuada a la función que desemos graficar.
#************* Cuando vayamos a graficar, también hay que tener cuidado cuántas y cuales dimensiones estamos
#************* graficando. En el caso de que tengamos 1 dimensión, graficamos los datos que obtenemos vs el tiempo
#************* en el caso de tengamos 2 dimensiones, graficamos en pares los valores que vamos obteniendo con dos listas
#************* diferentes.
def EulerND(f,x0,t0,tf,dt): #x0 es un vector NDimensional
    T=list()
    X=list() #Esta va a ser una lista de listas, cada elemento lista dentro de este, son los valores de una dimension
    #Necesito saber el tamano de X, y eso le definirá el tamaño de de x0
    #Como generalizamos desde 1 a N, entonces aplicamos el siguiente while True para usar el error de sólo tomar un valor
    #y operar desde su longitud, porque la función len() no es aplicable a variables de un sólo término
    #entonces, si X0 con sólo un término es una condición inicial para 1 dimensión, usemos el error de len() como filtro
    #para usar Euler en 1 dimensión.
    while True:
        try:
            len(x0)
            print("x0 Es de un vector")
            for i in range(len(x0)):
                lista_auxiliar = list()
                X.append(lista_auxiliar)
                X[i].append(x0[i])
            # Ya tenemos a X del tamaño requerido
            t = t0
            x = x0
            while (t < tf):
                x = x + f(x) * dt  ## x es un vector de ND
                t = t + dt
                for i in range(len(x)):
                    X[i].append(x[i])
                T.append(t)
            return X, T
            break
        except TypeError:
            print("X0 Es de un solo valor")
            T.append(t0)
            X.append(x0)
            t = t0
            x = x0
            while (t < tf):
                x = x + f(x) * dt
                t = t + dt
                X.append(x)
                T.append(t)
            return X, T

            break


def Logistica(P):
    r = .5
    K = 50
    return r*P*(1 - float(P)/float(K))

def Malthus(P):
    r = 1
    return r*P

def OsciladorSimple(x):  # x es un vector en 2D  (x,v)
    w0 = 1
    y = np.array(np.zeros(2))
    y[0] = x[1]
    y[1] = -w0 * x[0]
    return y


########Condiciones para el oscilador simple

x0 = np.array([1,0]) 
x0 = 1,0
t0 = 0
"""
# P = Euler1D(Malthus,p0,t0,10,0.1)
t0 = 0
p0 = 2

#X,T = EulerND(OsciladorSimple,p0,t0,10,0.1)
"""
X,T = EulerND(OsciladorSimple,x0,t0,15,0.0001)
#plt.plot(T,X)

plt.plot(X[0],X[1])
#plt.plot(2,1,'r^')
#plt.plot(X1,X2,'b.')
#plt.plot(x0[0],x0[1],'ro')
plt.show()
plt.clf()




