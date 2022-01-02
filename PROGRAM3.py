import random
import math
import numpy


#funkcija, ki izracuna teoreticno mejo za optimalno dimenzijo, na katero se zmanjsa. Slikamo iz dimenzije d v dimenzijo k. 
def spodnjameja_k(n, epsilon):
   return math.ceil(8*math.log(n) / (epsilon**2)) # ceil...vrne zgornjo mejo x kot integral. 


#generiraj točke kot matriko velikosti dxn (d...dim iz katere slikamo, n...št. točk)
# d = št. vrstic, n = št. stolpcev
def randomMatrika(d, n):
   return numpy.random.normal(0, 1, size=(d, n))


import numpy as np 

# podatki so vektorji oz točke (v matriki)

# np.linalg.norm(podatki - podatki[:,None], axis=-1) 

# Formula za izračun norm vektorjev, ki so podani kot vrstice, med vsemi vektorji


def randomPodprostor(podprostorDimenzija, prostorDimenzija):
   return numpy.random.normal(0, 1, size=(podprostorDimenzija, prostorDimenzija))


def jltransformacija(podatki, podprostorDimenzija):  # projekcija matrike iz višje dimenzije v manjšo
   prostorDimenzija = len(podatki)  # dimenzija 
   A = randomPodprostor(podprostorDimenzija, prostorDimenzija)
   return (1 / math.sqrt(podprostorDimenzija)) * A.dot(podatki)   
   

#######################
# 50 točk, epsilon 0.5, d = 200
k2 = spodnjameja_k(50, 0.5) #126, vzemimo k=130

M = randomMatrika(200,50) # matrika velikosti 200x50

D = M / numpy.linalg.norm(M, axis=0) # normirala stoplce v matriki M 

#preslikana matrika G velikosti 130x200 
G = jltransformacija(D, 130)
# G.shape # 130x50

x = numpy.linalg.norm(G, axis=0)
X = x*x

# izračun absolutne vrednosti razlik norm stoplpcev v G in 1 
abs(1-X)

preštejemo = abs(1-X)>0.5 # večje od epsilon, v našem primeru je to 0.5
število_primerov = preštejemo.sum()
delež = število_primerov/(50)  #0 

# Torej verjetnost je manjša od 0,5


# 
(G.T[0]) #prvi vektor v matriki G dolžine 130 

#------------------------------
# n=50, epsilon 0.2, d = 200
k3 = spodnjameja_k(50, 0.2) #783, vzemimo k=790
M3 = randomMatrika(200,50) 
D3 = M3 / numpy.linalg.norm(M3, axis=0) # normirala stoplce v matriki M 
G3 = jltransformacija(D3, 790)
x3 = numpy.linalg.norm(G3, axis=0)
X3 = x3*x3
preštejemo3 = abs(1-X3)>0.2 
število_primerov3 = preštejemo3.sum()
delež3 = število_primerov3/(50)  #0.0


# n=500, epsilon 0.5, d = 200
k4 = spodnjameja_k(500, 0.5) #199, vzemimo k=200
M4 = randomMatrika(200,500) 
D4 = M4 / numpy.linalg.norm(M4, axis=0) # normirala stoplce v matriki M 
G4 = jltransformacija(D4, 200)
x4 = numpy.linalg.norm(G4, axis=0)
X4 = x4*x4
preštejemo4 = abs(1-X4)>0.5
število_primerov4 = preštejemo4.sum()
delež4 = število_primerov4/(500)  #0.0

# n=500, epsilon 0.1, d = 200
k5 = spodnjameja_k(500, 0.1) #4972, vzemimo k=5000
M5 = randomMatrika(200,500) 
D5 = M5 / numpy.linalg.norm(M5, axis=0) # normirala stoplce v matriki M 
G5 = jltransformacija(D5, 5000)
x5 = numpy.linalg.norm(G5, axis=0)
X5 = x5*x5
preštejemo5 = abs(1-X5)>0.1
število_primerov5 = preštejemo5.sum()
delež5 = število_primerov5/(500)  #0.0


# n=500, epsilon 0.9, d = 200
k6 = spodnjameja_k(500, 0.9) #62, vzemimo k=70
M6 = randomMatrika(200,500) 
D6 = M6 / numpy.linalg.norm(M6, axis=0) # normirala stoplce v matriki M 
G6 = jltransformacija(D6, 70)
x6 = numpy.linalg.norm(G6, axis=0)
X6 = x6*x6
preštejemo6 = abs(1-X6)>0.9
število_primerov6 = preštejemo6.sum()
delež6 = število_primerov6/(500)  #0.0

# n=500, epsilon 0.2, d = 500
k7 = spodnjameja_k(500, 0.2) #1243, vzemimo k=1300
M7 = randomMatrika(500,500) 
D7 = M7 / numpy.linalg.norm(M7, axis=0) # normirala stoplce v matriki M 
G7 = jltransformacija(D7, 1300)
x7 = numpy.linalg.norm(G7, axis=0)
X7 = x7*x7
preštejemo7 = abs(1-X7)>0.2
število_primerov7 = preštejemo7.sum()
delež7 = število_primerov7/(500)  #0.0
