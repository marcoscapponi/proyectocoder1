def suma(numero1, numero2):
    return numero1 + numero2
resultado = suma(7, 5)
print(resultado)
print(suma(7,5))

def resta(a, b):
    return a - b
resultado2 = resta(15, 12)
print(resultado2)
print(resta(12, 15))

def resta2(a, b, c):
    return a - b - c
resultado3 = resta2(a=15, b=12, c=2)
print(resultado3)
resultado3bis = resta2(c=2, a=15, b= 12)
print(resultado3bis)

def resta3(a=10, b=5):
    return a - b
resultado4 = resta3()
print(resultado4)

def doblar_numero(numero):
    numero *= 2
numero = 10
doblar_numero(numero)
print(numero)

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
lista_de_nico = [10,50,100]
doblar_valores(lista_de_nico)
print(lista_de_nico)

def suma2(*args):
    s = 0
    for arg in args:
        s += arg
    return s
suma2(1, 3, 4, 2)
print(suma2(1, 3, 4, 2))

def suma3(**kwargs):
    ss = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        ss += value
    return ss
print(suma3(a=3, b=10, c=3))

def unidad_de_medida(*args):
    if len(args) == 1:
        milimetros = args[0]
        metros = milimetros / 1000
        centimetros = milimetros / 10
        return metros, centimetros, milimetros
    elif len(args) == 3:
        metros, centimetros, milimetros = args
        total_milimetros = metros * 1000 + centimetros * 10 + milimetros
        return total_milimetros
    else:
        return "numero incorrecto de argumentos. la funcion acepta 1 o 3 argumentos"
    
print(unidad_de_medida(5000))
print(unidad_de_medida(2, 50, 300))

def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("Booooooom!")
    print("Fin de la funcion", numero)
cuenta_regresiva(5)

def factorial(numero):
    print("valor inicial --> ", numero)
    if numero > 1:
        numero = numero * factorial(numero - 1)
    print ("valor final --> ", numero)
    return numero
factorial(5)