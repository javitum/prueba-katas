'''Supongamos que tienes un largo parterre en el que algunas de las parcelas están plantadas y otras no. 
Sin embargo, las flores no pueden ser plantadas en parcelas adyacentes - competirían por el agua y ambas morirían.

Dado un parterre (representado como una matriz que contiene 0 y 1, donde 0 significa vacío y 1 significa no vacío), 
y un número n, regrese si se pueden plantar n nuevas flores en él sin violar la regla de no-adjuntar flores.'''

# Escribe aqui tu funcion , parterre sera una lista con ceros y unos exclusivamente, y n un numero entero positivo (no borrar)
def canPlaceFlowers(parterre, n):
#escribe aqui en código de tu funcion (borrar)
    

    

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
