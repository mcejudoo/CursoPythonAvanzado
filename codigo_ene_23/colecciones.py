"""
Colecciones:  Se  piden  dos  números,  uno  menor  que  10  y  otro  
mayor  que  100.  El  primer número  representa  el  número  de  
intervalos  y  hay  que  calcular  los  rangos  de  los  intervalos según 
 el  segundo número.  Por  ejemplo:  n1  =  4,  n2  =  100.  Los  rangos  
 serían  de  0..24,  25..49, 50..74, 75..99.Después se generan números al azar 
 que no sobrepasen el número n2 y se almacenan en cada intervalo.  
 Luego  listar  los  intervalos  con  los  números  que  se  han  recogido.
 Hay  que  clasificar los números en el intervalo adecuado.
"""

from random import randint

n1=4
n2=100
aleatorio = [randint(0,n2-1) for _ in range(30)]
print(aleatorio[:5]) # slicing: L[ini:fin-1:salto]

# Generar los intervalos:


# Repartir los números aleatorios en cada intervalo:

