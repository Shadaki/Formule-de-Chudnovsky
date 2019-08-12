# Formule de Chudnovsky

![](https://raw.githubusercontent.com/sagessylu/Formule-de-Chudnovsky/master/pi_Chudnovsky.jpg | width=750)

J'utilise la méthode de Héron pour calculer la racine carrée d'un nombre :

```python
from decimal import *
n = int(input())
getcontext().prec = 1000
x = Decimal(1)
for i in range(40):
    x = Decimal((x+n/x)/2)
print(x)
```