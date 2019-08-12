from math import *
from decimal import *

nb=int(input("Combien de décimales de π voulez-vous ? "))
getcontext().prec=nb+1

def racine(n,prec):
    x=Decimal(1)
    for i in range(prec):
        x=Decimal((x+n/x)/2)
    return x

pi=Decimal(0)
for k in range(nb//13+1):
    a=Decimal((-1)**k*factorial(6*k)*(13591409+545140134*k))
    b=Decimal(factorial(3*k)*factorial(k)**3*640320**(3*k))
    pi+=Decimal(a/b)
pi=Decimal(426880*racine(10005,nb)/pi)

print(pi)
