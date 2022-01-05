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

# Program za izračun 
def program(epsilon,n,C,i,j):
   število_vseh_primerov = []
   #deleži_odstotek = []
   deleži = []
   delta_drži = []
   for m in range(i,j+1):
    k = spodnjameja_k(n, epsilon) #izračun dimenzije k, za 50 točk in poljuben epsilon
    d = k + 100*m     # za dimenzijo d vzamemo dimenzijo k in jo povečamo za nek faktor*100
    M = randomMatrika(d,C*n*n)  
    D = M / numpy.linalg.norm(M, axis=0)
    G = jltransformacija(D, k)
    x = numpy.linalg.norm(G, axis=0)
    X = x*x
    preštejemo = abs(1-X)>epsilon
    število_primerov = preštejemo.sum()  #število primerov odstopanj 
    delež = število_primerov/(C*n*n)
    preštejemo_delta = delež < (1 /(n*n))   # delež < delta < 1 /(n*n)
    #delež_odstotek = delež * 100
    število_vseh_primerov.append(število_primerov)
    deleži.append(delež)
    #deleži_odstotek.append(delež_odstotek)   
    delta_drži.append(preštejemo_delta)
   return število_vseh_primerov, deleži, delta_drži

#POSKUSI Z PROGRAMOM 

#program(0.5,50,40,1,3)
# ([32, 17, 33], [0.00032, 0.00017, 0.00033], [True, True, True])
#program(0.5,50,40,1,3)
#([22, 37, 22], [0.00022, 0.00037, 0.00022], [True, True, True])

# POSKUSI brez programa

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