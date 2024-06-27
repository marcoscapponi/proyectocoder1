cadena = "hola mundo, como estas mundo?"
print(cadena)
print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize()) ## mayuscula a la primer letra
print(cadena.title()) ## mayuscula a todas las palabras
print(cadena.count("o")) ## cuenta los caracteres o palabras entre commillas
print(cadena.find("mundo")) ## busca la primer palabra
print(cadena.rfind("mundo")) ## busca la ultima palabra
print(cadena.split()) ## separa todas las palabras
print(" ".join(cadena)) ## lo que ponga entre comillas se va a representar entre todas las letras
print(cadena.strip(" ")) ## borra los caracteres de mas
print(cadena.replace("?", "!")) ## remplaza caracteres

###################################################################
## LISTAS

numeros = [1, 2, 3, 4]
print(numeros)
print(numeros.clear())
numeros = [1, 2, 3, 4]
numeros2 = [5, 6, 7, 8]
numeros.extend(numeros2)
print(numeros + numeros2)
numeros.insert(0,0)
print(numeros)
numeros.reverse()
print(numeros)

desordenados = [8,23,345, 1, 3,2]
desordenados.sort()
print(desordenados)

##gordon lanzó sucurva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies-le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista


segundo = "gordon lanzó sucurva&strawberry ha fallado por un pie! - grito Joe Castiglione&dos pies-le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
primero = segundo.replace("&", "\n-")


primero = primero.replace("gordon", "Gordon").replace("strawberry", "Strawberry")
print(primero)

###############################################################################

set1 = {1, 2, 3, 4}
print(set1)
set2 = set1.copy()
print(set2)
set1.isdisjoint(set2)
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
set3 = {1, 2}
print(set1.issuperset(set3))
print(set1.difference(set3))
print(set1.difference_update(set3))

#################################################################################

##Ejemplo 1:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.union(my_set_2)
print(my_new_set)

##Ejemplo 2:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.intersection(my_set_2)
print(my_new_set)

##Ejemplo 3:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.difference(my_set_2)
print(my_new_set)

##Ejemplo 4:
my_set_1 = set([1, 2, 3])
my_set_2 = set([3, 4, 5])
my_new_set = my_set_1.difference_update(my_set_2)
print(my_new_set)

############################################################

divisas = {"dolar":"$", "Euro":"E", "Libra":"L"}
print(divisas.get("dolar", "no hay dolar"))

#############################################################

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
lista_2 = list(set(lista))
print(lista_2)
lista_2.sort()
print(lista_2)
for i in lista_2:
    if i % 2 != 0:
       lista_2.remove(i)
print(lista_2)
print(sum(lista_2))
lista_2.insert(0,sum(lista_2))
print(lista_2)


