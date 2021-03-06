'''Supongamos que tienes un largo parterre en el que algunas de las parcelas están plantadas y otras no. 
Sin embargo, las flores no pueden ser plantadas en parcelas adyacentes - competirían por el agua y ambas morirían.

Dado un parterre (representado como una matriz que contiene 0 y 1, donde 0 significa vacío y 1 significa no vacío), 
y un número n, regrese si se pueden plantar n nuevas flores en él sin violar la regla de no-adjuntar flores.'''

# Parterre sera una lista con ceros y unos exclusivamente, y n un numero entero positivo (no borrar)
#Escribe aqui tu funcion (no borrar)
def canPlaceFlowers(parterre, n):
    parterre=[0]+parterre+[0]
    plantadas_inicio=parterre.count(1)
    for i in range(1, len(parterre)-1):
        if parterre[i-1]==0 and parterre[i]==0 and parterre[i+1]==0:
            parterre[i]=1
    plantadas_final=parterre.count(1)
    return plantadas_final-plantadas_inicio>=n

# Inicio de testeo de codigo (no borrar)

import unittest
import timeit

class PruebasFuncion(unittest.TestCase):
    def test1(self):
        parametros=[
        ('prueba1',[1,0,0,0,1],1, True, ''), 
        ('prueba2',[1,0,0,0,1],2, False, ''), 
        ('prueba3',[0,0,1,0,0,0,0,1,0,0,1],2, True, ''), 
        ('prueba4',[0,0,1,0,0,0,0,1,0,0,1],3, False, ''), 
        ('prueba5',[1,1,0,0,0,0,1,0,0,0,0,0,1,0],3, True, ''), 
        ('prueba6',[1,1,0,0,0,0,1,0,0,0,0,0,1,0],4, False, '')]
        for p1, p2,  p3,  p4 , p5 in parametros:
            with self.subTest():
                self.assertEqual(canPlaceFlowers(p2, p3), p4, f'{p1}---{p5}')

if __name__ == '__main__':
    resultado=unittest.main(verbosity=2, exit=False)
    if len(resultado.result.failures)==0:
        print('Todos los test correctamente pasados. Continuamos la prueba')
        t = timeit.timeit("canPlaceFlowers([1,1,0,0,0,0,1,0,0,0,0,0,1,0],3)", "from __main__ import canPlaceFlowers")
        print(f'Se tardan {t} segundos en ejecutar la función 1.000.000 de veces')
    else:
        print(f'Ha habido {len(resultado.result.failures)} error/es')
        for n in resultado.result.failures:
            print(n[1])
