# Formule de Chudnovsky

![](https://raw.githubusercontent.com/sagessylu/Formule-de-Chudnovsky/master/pi_Chudnovsky.jpg)

J'utilise le code suivant pour calculer la racine carrée d'un nombre (méthode de Héron) :

```
from decimal import *
n = int(input())
getcontext().prec = 1000
x = Decimal(1)
for i in range(40):
    x = Decimal((x+n/x)/2)
print(x)
```