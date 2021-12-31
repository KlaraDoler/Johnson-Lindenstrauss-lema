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
   prostorDimenzija = len(podatki[0])  # dimenzija stolpecv 
   A = randomPodprostor(podprostorDimenzija, prostorDimenzija)
   return (1 / math.sqrt(podprostorDimenzija)) * A.dot(podatki.T).T   #zadnji T ni potreben 
   

#######################
# 50 točk, epsilon 0.5, d = 200
k2 = spodnjameja_k(50, 0.5) #126, vzemimo k=130

M = randomMatrika(130,200)

#preslikana matrika G
G = jltransformacija(M, 130)

normeM = np.linalg.norm(M - M[:,None], axis=-1)   # norme vektorjev kot vrstice
normeG = np.linalg.norm(G - G[:,None], axis=-1)


# formula za norme vektorjev kot stoplcev x = np.linalg.norm(M, axis=0)

r2 = abs(normeM - normeG)

#preštejmo koliko razlik je manjših od 1+epsilon?
#delež primerov, pri katerih se norma stolpca dobljene matrike razlikuje od 1 za več kot ε
preštejemo = abs(r2-1)>0.5
število_primerov = preštejemo.sum() #10854
# vseh elementov v r2 je 130*130=16900
#delež = število_primerov/(d*d)
delež = število_primerov/(16900) #0.6422