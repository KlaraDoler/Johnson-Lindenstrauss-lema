import random
import math
import numpy
  
#funkcija, ki izracuna teoreticno mejo za optimalno dimenzijo, na katero se zmanjsa. Slikamo iz dimenzije d v dimenzijo k. 
def spodnjameja_k(n, epsilon):
   return math.ceil(8*math.log(n) / (epsilon**2)) # ceil...vrne zgornjo mejo x kot integral. 

# Najprej definiramo nakljucni podprostor z vzorcenjem matrike ustrezne velikosti 
# z normalno porazdeljenimi vnosi. Ogledale smo si 3 različne primere: 

# VELIKOST MATRIKE DXK (D je dimenzija prostora in K je dimenzija podprostora) in TRANSFORMACIJA

def randomPodprostor(podprostorDimenzija, prostorDimenzija):
   return numpy.random.normal(0, 1, size=(podprostorDimenzija, prostorDimenzija))

#vrednosti v matriki so naključno porazdljene z normalno porazdelitvijo N(0,1)

#izvajanje JLT je preprosto mnozenje matrik, podatki = vzorec - matrika ali vektor,dimenzija 

def jltransformacija(podatki, podprostorDimenzija):  # projekcija matrike iz višje dimenzije v manjšo
   prostorDimenzija = len(podatki[0])  # dimenzija stolpecv 
   A = randomPodprostor(podprostorDimenzija, prostorDimenzija)
   return (1 / math.sqrt(podprostorDimenzija)) * A.dot(podatki.T).T 


# VELIKOST MATRIKE DXD IN TRANSFORMACIJA
def randomprostor(dimenzija_d):  # matrika velikosti dxd z normalno porazdeljenimi vnosi 
    return numpy.random.normal(0, 1, size=(dimenzija_d, dimenzija_d))

def jltransformacija(podatki, podprostorDimenzija):  # projekcija matrike iz višje dimenzije v manjšo
   prostorDimenzija = len(podatki[0])  # dimenzija stolpecv 
   A = randomPodprostor(podprostorDimenzija, prostorDimenzija)
   return (1 / math.sqrt(podprostorDimenzija)) * A.dot(podatki.T).T 


# VEKTOR in TRANSFORMACIJA 
def randomvektor(dimenzija_d):  # vektor velikosti 1xd z normalno porazdeljenimi vnosi, lahko bi dali tudi dx1
    return numpy.random.normal(0, 1, size=(1, dimenzija_d))


def jltransformacija(podatki, podprostorDimenzija):  # projekcija matrike iz višje dimenzije v manjšo
   prostorDimenzija = len(podatki[0])  # dimenzija stolpecv 
   A = randomPodprostor(podprostorDimenzija, prostorDimenzija)
   return (1 / math.sqrt(podprostorDimenzija)) * A.dot(podatki.T).T 


#evklidska razdalja med vektorji 
import numpy as np

# a = np.array((1, 2, 3)) PRIMER VEKTORJA
# b = np.array((4, 5, 6))

dist = np.linalg.norm(a-b) # matrična ali vektorska norma 

# PREIZKUS PROGRAMA NA 2 TOČKAH = VEKTORJIH

# naprej sva poračunali koliko more biti spodnja meja za k, če želimo da 
# je epsilon 0.1 in imamo število točk = 2 (n = 2)

spodnjameja_k(2, 0.1) #555, torej podprostor mora biti dimenzije vsaj 555

# vzamemo vektorja a in b oba sta velikosti 1x1000

 a = randomvektor(1000)
 b = randomvektor(1000)

 dist = np.linalg.norm(a-b)  # 44.164153027476395 (evkildska razdalja)

# preslikava iz prostora 1000 na 560
 c = jltransformacija(a,560)
 d = jltransformacija(b,560) 

 dist1 = np.linalg.norm(c-d) # 44.156530854980545 (evklidska razdalja)

 # PREIZKUS PROGRAMA, KO SLIKAMO MATRIKO 560X1000 V MATRIKO 560x560 

 spodnjameja_k(10,0.1) # ko vzamemo n = 10 vektorjev,rabimo dimenzijo za k večjo od 1843

 A = randomPodprostor(560,1000) 
 B = jltransformacija(A, 560)
 
 # za izračun razdalje med vektorji v matriki 

from scipy.spatial.distance import pdist

c = squareform(pdist(A)) # razdalja med vektorji (vrsticami) v matriki A

d = squareform(pdist(B)) # razdalje med vektorji v matriki B 

c-d  =  # matrika razlik razdalji, vidimo da se razdalje razlikujejo za vrednosti med 1-0.1 in 1+0.