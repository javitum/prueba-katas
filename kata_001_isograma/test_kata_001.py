import os
import unittest
import timeit

repeticiones=100000
kata='kata_001'
funcion='is_isogram'
descripcion='''Un isograma es una palabra que no tiene letras repetidas, consecutivas o no consecutivas. 
Implementar una función que determine si una cadena que contiene sólo letras es un isograma. 
Supongamos que la cadena vacía es un isograma. Ignorar las mayusculas y minusculas de las letras.'''

archivos = [ archivo for archivo in os.listdir() if archivo.startswith(kata)]
usuarios=[usuario[9:-3] for usuario in archivos]
librerias=[usuario[:-3] for usuario in archivos]

datos=[]
for i in range (len(archivos)):
    datos.append([usuarios[i], librerias[i], archivos[i]])
print(datos)


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
                self.assertEqual(fun(p2), p3, f'{p1}---{p4}')


for dato in datos:
    exec(f"from {dato[1]} import {funcion} as fun")
    #Comprobación de errores
    resultado=unittest.main(verbosity=2, exit=False)
    errores=len(resultado.result.failures)
    dato.append(errores)
    
    #Tiempo de ejecución de la funcion a testear
    t = timeit.timeit(f"{funcion}('Dermatoglyphics')", f"from {dato[1]} import {funcion}", number=repeticiones)
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
print(descripcion)
print('    Usuario                              Errores       Tiempo(s)        Lineas')
for dato in datos:
    print(f'{dato[1]:35}    {dato[3]:02}         {dato[4]:7.4f}             {dato[5]:03}')
    

    
    
