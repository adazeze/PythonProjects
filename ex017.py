from math import hypot
co = float(input('Comproimento do cateto oposto: '))
ca = float(input('Comprimento do caceto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
