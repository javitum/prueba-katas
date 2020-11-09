import os
import unittest
import timeit

repeticiones=100000
kata='kata_002'
funcion='canPlaceFlowers'
descripcion='''Supongamos que tienes un largo parterre en el que algunas de las parcelas 
están plantadas y otras no. 
Sin embargo, las flores no pueden ser plantadas en parcelas adyacentes - 
competirían por el agua y ambas morirían.
Dado un parterre (representado como una matriz que contiene 0 y 1, donde 0 
significa vacío y 1 significa no vacío), y un número n, regrese si se pueden 
plantar n nuevas flores en él sin violar la regla de no-adjuntar flores.'''

archivos = [ archivo for archivo in os.listdir() if archivo.startswith('kata_002')]
usuarios=[usuario[9:-3] for usuario in archivos]
librerias=[usuario[:-3] for usuario in archivos]

datos=[]
for i in range (len(archivos)):
    datos.append([usuarios[i], librerias[i], archivos[i]])

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
                self.assertEqual(fun(p2, p3), p4, f'{p1}---{p5}')

for dato in datos:
    exec(f"from {dato[1]} import {funcion} as fun")
    #Comprobación de errores
    resultado=unittest.main(verbosity=2, exit=False)
    errores=len(resultado.result.failures)
    dato.append(errores)

    #Tiempo de ejecución de la funcion a testear
    t = timeit.timeit(f"{funcion}([1,1,0,0,0,0,1,0,0,0,0,0,1,0],3)", f"from {dato[1]} import {funcion}", number=repeticiones) 
    dato.append(t)

    #Número de líneas de la función
    texto_inicio_funcion = 'Escribe aqui tu funcion (no borrar)'
    texto_fin_funcion='Inicio de testeo de codigo (no borrar)'
    PosicionTexto = -1
    NumeroLinea = 0
    with open(dato[2], 'r') as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(texto_inicio_funcion)
            if PosicionTexto >= 0:
                linea_inicio=NumeroLinea
                continue
            PosicionTexto2 = line.find(texto_fin_funcion)
            if PosicionTexto2 >= 0:
                linea_final=NumeroLinea
                dato.append(linea_final-linea_inicio-1)
                break

    # Resultados 
print(f'{"KATA 002 PLANTAR FLORES":^70s}')
print(f'{"="*70}')
print(descripcion)
print(f'{"="*70}')
print('    Usuario                         Errores     Tiempo(s)  Lineas')
for dato in datos:
    print(f'{dato[0]:<25}\t{dato[3]:8}{dato[4]:15.4f}{dato[5]:8}')
    

    
    
