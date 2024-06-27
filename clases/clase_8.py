# def saludar_con_nombre(nombre):
#     saludando = print("hola {}! como estas?".format(nombre))
#     return saludando

# saludar_con_nombre("Juan")



# def ciudad(ciudat):
#     nombre_ciu = print("hola bienvenido a ", ciudat)
#     return

# ciudad("buenos aires")


# def promedio(muestra):
#     return sum(muestra)/len(muestra)


# print(promedio([1, 2, 3, 4, 5]))

# def es_multiplo(num1, num2):
#     if num1 % num2 == 0:
#         print("es multiplo")
#     elif num2 % num1 == 0:
#         print("es multiplo")
#     else:
#         print("no es multiplo")
#     return

# es_multiplo(5,4)


# def anio_bisiesto():
#     while True:
#         while True:
#             entrada = input("Ingrese el anio para identificar si es bisiesto: ")
            
#             if entrada.isdigit():
#                 anio = int(entrada)
#                 print("gracias por ingresar el numero correctamente")

#                 if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
#                     print("El anio ", anio, "es bisiesto")
#                 else:
#                     print("el anio ", anio, "no es bisiesto")
#                 break
#             else:
#                 print("has ingresado un numero erroneo")

#         consulta_nueva = input("deseas consultar nuevamente? (si/no):")
#         if consulta_nueva.lower() != "si":
#             print("fin del programa.")
#             break

# anio_bisiesto()

def saludar_con_nombre(nombre):
    saludando = print("Hola {}! Como estas?" .format(nombre))
    return saludando

saludar_con_nombre("juan")

variable_test = 10
def test():
    variable_test = 155
    print(variable_test)
    return variable_test
test()

def saludar_con_nombre2(nombre):
    saludando = print("Hoola {}! Commo estas?" .format(nombre))
    return saludando
    print("HOla mundo")
saludar_con_nombre2("juan")

def lista():
    return [1, 2, 3, 4, 5]
print(lista())

variable = lista()
variable[1:4]
print(variable[1:4])

def test():
    return "Python", 20, [1,2,3]
print(test())

def suma(numero1, numero2):
    return numero1 + numero2
r = suma(7, 5)
print(r)