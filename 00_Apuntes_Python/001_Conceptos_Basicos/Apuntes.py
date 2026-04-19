## 1) Declaración de variables (tipos de datos) ##
numeroEntero = 10 #No considera decimales
numeroFlotante = 3.1416 #Considera hasta 15 digitos de forma confiable
string = 'WAZAAAA' #Secuencia de caracteres delimitado en comillas
valorBooleano = True #Valo del tipo True/False
valorConjunto = {7, 'hello', 8.5} #Un set de valores unicos y sin orden y editable
valorTupla = ('apple', 4.5, 7) #colección ordenada e inmutable de valores unicos
valorDiccionario = {'name': 'John Doe', 'age': 28} #Colección de pares clave-valor encerrados entre llaves
rango = range(5) #Secuencia de numeros (casi siempre usadas en bucles)
lista = [22, 'Hello world', 3.14, True] #Coleccion ordenada de elementos que soporta diferentes tipos de datos
vacio = None #Un tipo de valor que representa la ausencia de valor 

print(numeroEntero) #Inmutable
print(numeroFlotante) #Inmutable
print(string) #Inmutable 
print(valorBooleano) #Inmutable
print(valorConjunto)
print(valorTupla) #Inmutable
print(valorDiccionario)
print(rango) #Inmutable
print(lista)
print(vacio)

##NOTA
#Para conocer el tipo de dato de una variable se usa la funcion type()
#cuyo argumento es el nombre de la variable. -> type(numeroEntero) -> <class 'int'>
#Por otra parte, la funcion isinstance() verifica si la variable corresponde
#al tipo de dato con el que comparas. ->isinstance(valorBooleano, bool) -> <class True>

print("\n",type(rango))
print(isinstance(valorBooleano, bool))

## 2) Diferentes formas de imprimir en consola ##

numero_entero = 45 
nombre1 = 'Juan'
nombre2 = 'Luis'
apellido1 = 'Montes'
apellido2 = 'Gutierrez'
color = 'azul'


print('\n1)Hola Mundo, wazaaa') #Impresion clasica (un argumento)
print('\n2)Me presento', 'mi nombre', 'es Juan') #Impresion con multiples argumentos
print('\n3)Mi color favorito es ' + color + ' y me llamo ' + nombre1)

'''
Esta es la segunda forma de declarar comentarios.
 NOTA: Se usa '#' para comandos de una sola linea, 
 en cambio las comillas triples para comandos multilinea.

A lo que veniamos.
Esta version de codigo genera error, ya que 'numero_entero' es numerico no string
y si queremos concatenar solo se pueden usar strings

print('\nMi color favorito es '+ color + ' y mi numero favorito el ' + numero_entero) 
'''

print('\n4)Hola. mi nombre completo es', nombre1, nombre2, apellido1, apellido2) #Impresion con uso de variables
print(f'\n5)Buenas, me llamo {nombre1}, tengo un amigo que se llama {nombre2}') #Impresion usando 'f' para insertar directamente variales en la zona de interes
print("""\n6)Se pueden hacer
impresiones de tipo
multilinea XD
""")

nombre_completo = nombre1
nombre_completo += nombre2

print("\n7)Me llamo", nombre_completo) #Impresion concatenando las variables