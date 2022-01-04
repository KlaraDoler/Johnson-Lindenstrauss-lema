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


def randomPodprostor(podprostorDimenzija, prostorDimenzija):
   return numpy.random.normal(0, 1, size=(podprostorDimenzija, prostorDimenzija))


def jltransformacija(podatki, podprostorDimenzija):  # projekcija matrike iz višje dimenzije v manjšo
   prostorDimenzija = len(podatki)  # dimenzija 
   A = randomPodprostor(podprostorDimenzija, prostorDimenzija)
   return (1 / math.sqrt(podprostorDimenzija)) * A.dot(podatki)   
   

# POSKUSI

## 50 točk, C=40, 100000 stolpcev, epsilon 0.5, d = 200
k2 = spodnjameja_k(50, 0.5) #126, vzemimo k=130
M = randomMatrika(200,100000) # matrika velikosti 200x100000
D = M / numpy.linalg.norm(M, axis=0) # normirala stoplce v matriki M 
#preslikana matrika G velikosti 130x100000
G = jltransformacija(D, 130)
# G.shape # 130x50
x = numpy.linalg.norm(G, axis=0)
X = x*x
# izračun absolutne vrednosti razlik norm stoplpcev v G in 1 
abs(1-X)

preštejemo = abs(1-X)>0.5 # večje od epsilon, v našem primeru je to 0.5
število_primerov = preštejemo.sum() #26
delež = število_primerov/(100000)  #0.00026 
# Torej verjetnost je manjša od 0,5


## n=50, C=40, 100000 stolpcev, d=500, epsilon=0.2
k3 = spodnjameja_k(50, 0.2) #783, vzemimo k=790
M3 = randomMatrika(200,100000) 
D3 = M3 / numpy.linalg.norm(M3, axis=0) # normirala stoplce v matriki M 
G3 = jltransformacija(D3, 790)
x3 = numpy.linalg.norm(G3, axis=0)
X3 = x3*x3
preštejemo3 = abs(1-X3)>0.2 
število_primerov3 = preštejemo3.sum() #20
delež3 = število_primerov3/(100000)  #0.0002


## n=50, C=40, 100000 stolpcev, d=500, epsilon=0.5
k = spodnjameja_k(50, 0.5) #126, vzemimo k=130
M7 = randomMatrika(500,100000)
D7 = M7 / numpy.linalg.norm(M7, axis=0) # normirala stoplce v matriki M 
G7 = jltransformacija(D7, 130)
x7 = numpy.linalg.norm(G7, axis=0)
X7 = x7*x7
preštejemo7 = abs(1-X7)>0.5
število_primerov7 = preštejemo7.sum() #27
#delež7 = število_primerov7/(100000*1000000)  #2.7e-10
delež7 = število_primerov7/(100000) # 0.00027