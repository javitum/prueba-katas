'''Un isograma es una palabra que no tiene letras repetidas, consecutivas o no consecutivas. 
Implementar una función que determine si una cadena que contiene sólo letras es un isograma. 
Supongamos que la cadena vacía es un isograma. Ignorar las mayusculas y minusculas de las letras.'''

# Escribe aqui tu funcion (no borrar)
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True 
# Inicio de testeo de codigo (no borrar)

import unittest
import timeit

class PruebasFuncion(unittest.TestCase):
    def test1(self):
        parametros=[
        ('prueba1','Dermatoglyphics', True, ''), 
        ('prueba2','isogram', True, ''), 
        ('prueba3','aba', False, "los mismos caracteres no pueden reperirse"), 
        ('prueba4',"moOse", False, "los mismos caracteres en mayusculas o minusculas no pueden reperirse"), 
        ('prueba5',"isIsogram", False, '' ), 
        ('prueba6',"", True, "Una cadena vacia es un isograma valido" )]
        for p1, p2,  p3,  p4 in parametros:
            with self.subTest():
                self.assertEqual(is_isogram(p2), p3, f'{p1}---{p4}')

if __name__ == '__main__':
    resultado=unittest.main(verbosity=2, exit=False)
    if len(resultado.result.failures)==0:
        print('Todos los test correctamente pasados. Continuamos la prueba')
        t = timeit.timeit("is_isogram('Dermatoglyphics')", "from __main__ import is_isogram")
        print(f'Se tardan {t} segundos en ejecutar la función 1.000.000 de veces')
    else:
        print(f'Ha habido {len(resultado.result.failures)} error/es')
        for n in resultado.result.failures:
            print(n[1])
