# Formule de Chudnovsky

J'utilise le code suivant pour calculer la racine carrée d'un nombre :

<code>
from decimal import *
n = int(input())
getcontext().prec = 1000
x = Decimal(1)
for i in range(40):
    x = Decimal((x+n/x)/2)
print(x)
</code>