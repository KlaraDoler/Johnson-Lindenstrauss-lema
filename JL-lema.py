import random
import math
import numpy


#funkcija, ki izracuna teoreticno mejo za optimalno dimenzijo, na katero se zmanjsa. Slikamo iz dimenzije d v dimenzijo k. 
def spodnjameja_k(n, epsilon):
   return math.ceil(8*math.log(n) / (epsilon**2)) # ceil...vrne zgornjo mejo x kot integral. 


#generira točke kot matriko velikosti dxn (d...dim iz katere slikamo, n...št. točk)
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
def program(epsilon, n, C, i, j, t=10):
    število_vseh_primerov = []
    deleži = []
    delta_drži = []
    for m in range(i,j+1):
        k = spodnjameja_k(n, epsilon) #izračun dimenzije k, za 50 točk in poljuben epsilon
        d = k + 100*m     # za dimenzijo d vzamemo dimenzijo k in jo povečamo za nek faktor*100
        M = randomMatrika(d,C*n*n)  
        D = M / numpy.linalg.norm(M, axis=0)
        število_primerov = 0
        for _ in range(t):    # uporabimo iste točke s t različnimi transformacijami
            G = jltransformacija(D, k)
            x = numpy.linalg.norm(G, axis=0)
            X = x*x
            preštejemo = abs(1-X)>epsilon
            število_primerov += preštejemo.sum()    #število primerov odstopanj 
        delež = število_primerov/(C*n*n*t)
        preštejemo_delta = delež < (1 /(n*n))   # delež < delta < 1 /(n*n)
        število_vseh_primerov.append(število_primerov)
        deleži.append(delež)   
        delta_drži.append(preštejemo_delta)
    return število_vseh_primerov, deleži, delta_drži



#POSKUSI S PROGRAMOM 
# spreminjanje vrednosti epsilon

# program(0.2,50,40,1,3,10)
# ([89, 101, 111], [8.9e-05, 0.000101, 0.000111], [True, True, True])

#program(0.3,50,40,1,3)  
#([120, 145, 140], [0.00012, 0.000145, 0.00014], [True, True, True])

#program(0.4,50,40,1,3)  
#([192, 196, 182], [0.000192, 0.000196, 0.000182], [True, True, True])

#program(0.5,50,40,1,3,10)
#([252, 305, 235], [0.000252, 0.000305, 0.000235], [True, True, True])

#program(0.8,50,40,1,3)      
#([525, 429, 457], [0.000525, 0.000429, 0.000457], [False, False, False])


import matplotlib
import matplotlib.pyplot as plt
# graf povprečnih števil odstopanj za n=50, C=40, epsilon={0.2, 0.3, 0.4, 0.5}, d=k+100
plt.plot([0.2, 0.3, 0.4, 0.5],[8.9,12.0,19.2,25.2])
plt.xlabel("Epsilon")
plt.ylabel("Povprečno število primerov")
plt.suptitle('Povprečno število odstopanj za različne epsilone')
plt.show()


# POSKUS 2 
# spreminjanje števila točk

#program(0.2,5,40,1,3,10)
#([98, 117, 114], [0.0098, 0.0117, 0.0114], [True, True, True])

#program(0.2,10,40,1,3,10)
#([107, 92, 109], [0.002675, 0.0023, 0.002725], [True, True, True])

#program(0.2,50,40,1,3,10)
#([89, 101, 111], [8.9e-05, 0.000101, 0.000111], [True, True, True])
