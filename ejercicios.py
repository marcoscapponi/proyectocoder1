#solicitar al usuario que ingrese nombres separados con coma
#nombres_ingresados = input("ingrese nombres separados con comas: ")

#crear conjunto apartir de los nombres
#conjunto_nombres = set(nombres_ingresados.split(","))
#print(conjunto_nombres)
#mostrar la cantidad de nombres unicos en el conjunto
#cantidad_nombres_unicos = len(conjunto_nombres)
#print("cantidad de nombres unicos: ", cantidad_nombres_unicos)


#inicializar el diccionario de inventario de productos
#inventarios = {
#    "Manzanas": 50,
#    "Bananas": 30,
#    "Peras": 40
#}

#agregar un nuevo producto al inventario
#nuevo_producto = input("ingrese el nombre de un nuevo producto: ")
#cantidad_nuevo_producto = int(input(f"ingresa la cantidad de {nuevo_producto}: "))
#inventarios[nuevo_producto] = cantidad_nuevo_producto
#print (inventarios)

#actualizar la cantidad de un producto existente
#producto_existente = input("ingrese el nombre del producto ya existente: ")
#nueva_cantidad_existente = int(input(f"ingresa la nueva cantidad de {producto_existente}: "))
#inventarios[nuevo_producto] = nueva_cantidad_existente
#print("inventario actualizado: ", inventarios)


#solicitar al usuario una oracion
#oracion = input("ingrese una accion: ")
#convertir la oracion en mayuscula
#oracion_mayuscula = oracion.upper()
#contar cuantas veces aparece la palabra "python" en la oracion
#contador_python = oracion.count("python")
#mostrar la oracion sin espacios en blanco al inicio y al final
#oracion_sin_espacios = oracion.strip()

#print("oracion en mayusculas: ", oracion_mayuscula)
#print("cantidad de veces python: ", contador_python)
#print("oracion sin espacios en blanco: ", oracion_sin_espacios)

#solicitar al usuario ingresar numeros separados por comas para cada conjunto
##numeros1 = set(input("ingrese numeros para el primer comjunto: ").split(","))
##numeros2 = set(input("ingrese numeros para el segundo comjunto: ").split(","))

#verificar si los conjumtos tienen elementos en comun
##tienen_elementos_comunes = numeros1.isdisjoint(numeros2)

#crear un conjuto con la union de ambos conjuntos
##union_conjuntos = numeros1.union(numeros2)

##print("que elementos tienen en comun? ", tienen_elementos_comunes)
##print("union de conjuntos: ", union_conjuntos)

# numero1 = (int(input("ingrese un numero entero: ", )))
# numero2 = (int(input("ingrese otro numero entero: ", )))

# if numero1 % 2 == 0 and numero2 % 2 == 0:
#     print("ambos son numeros pares")

# number = (int(input("ingrese un numero entero: ",)))
# if number % 2 == 0:
#     if number % 3 == 0 and number % 5 == 0:
#         print("es par y divisible por 3 y 5")
#     else:
#         print("es par pero no divisible")
# else:
#     print("ninguna de las anteriores")

###########################################################
# numeroEntero = (int(input("ingrese un numero entero")))
# if numeroEntero > 0:
#     if numeroEntero % 2 == 0:
#         print("es un numero positivo y par")
#     else:
#         print("es positivo pero inpar")
# elif numeroEntero < 0:
#     print("es menor a cero")
# else:
#     print("es igual a 0")

############################################################
 

# palabra = input("ingreser una palabra: ")
# vocales = ("aeiouAEIOU")
# cant_vocales = 0

# for letra in palabra:
#     if letra in vocales:
#         cant_vocales += 1
# else:
#     if cant_vocales == 0:
#         print("la palabra no tiene vocales.")
#     else:
#         print(f"la palabra tiene {cant_vocales} vocales.")

# palabras = input("ingrese una lista de palabras: ").split()

# for palabra in palabras:
#     if palabra == "salir":
#         break
#     elif palabra == "omitir":
#         continue
#     else:
#         print(palabra)
# else:
#     print("no se encontreo la palabra 'salir'.")

# inventario = {}
# num_productos = int(input("ingresa la cantidad de productos en el inventario a cargar: "))
# for _ in range(num_productos):
#     nombre = input("ingresa el nombre del producto: ")
#     cantidad = int (input(f"ingrese la cantidad de {nombre}: "))
#     inventario[nombre] = cantidad

# print("\ninventario:")
# total_productos = 0

# for producto, cantidad in inventario.items():
#     print(f"{producto}: {cantidad}")
#     total_productos += cantidad

# print("\nTotal de productos en el inventario: ", total_productos)

# contrasenia1 = input("ingrese una contrasenia: ")
# contrasenia2 = "python123"
# while contrasenia1 != contrasenia2:
#     print("contrasenia incorrecta")
#     contrasenia1 = input("ingrese una contasenia: ")
# else:
#     print("acceso concedido")


# numeros = []
# for numero in range(0, 21, 2):
#     numeros.append(numero)
# print(numeros)

# def area_rectangulo(base, altura):
#     return base * altura

# area = area_rectangulo(15,10)
# print("el area del rectangulo es: ", area)

# def area_circulo(radio):
#     return (radio **2) * 3.14
# area2 = area_circulo(5)

# def relacion(num1, num2):
#     if num1 > num2:
#         return 1
#     elif num1 < num2:
#         return -1
#     else:
#         return 0
    
# print(relacion(5,10))
# print(relacion(10,5))
# print(relacion(5,5))

# def intermedio(num1, num2):
#     return (num1 + num2) / 2
# punto_intermedio = intermedio(14, -12)
# print(f"el numero intermedio es {punto_intermedio}")

# def recortar(numero, limite_inf, limite_sup):
#     if numero < limite_inf:
#         return limite_inf
#     elif numero > limite_sup:
#         return limite_sup
#     else: 
#         return numero
    
# resultado = recortar(15, 0, 10)
# print(f"el resultado es: {resultado}")

# def separar(lista):
#     pares = []
#     impares = []
#     for num in lista:
#         if num % 2 == 0:
#             pares.append(num)
#         else:
#             impares.append(num)
#     return sorted(pares), sorted(impares)

# # Ejemplo de uso:
# numeros = [6, 5, 2, 1, 7]
# pares, impares = separar(numeros)
# print("Números pares:", pares)
# print("Números impares:", impares)

# def separar(lista):
#     pares = [num for num in lista if num % 2 == 0]
#     impares = [num for num in lista if num % 2 != 0]
#     pares.sort()
#     impares.sort()


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares, impares = separar(lista)
# print(f"pares: {pares}")
# print(f"impares: {impares}")

# x = 5
# while True:
#     x -= 1
#     print(x)
#     if x == 0:
#         break
# print("Fin del bucle")

# def ciudad(city):
#     print("hola bienvenido a ", city)

# ciudad("Buenos Aires")

# def calcular_media(numeros):
#     media = sum(numeros) / len(numeros)
#     print(media)
#     return media
# numeros = [1, 2, 3, 4, 5]
# calcular_media(numeros)

# def es_multiplo():
#     while True:
#         num1 = int(input("ingrese un numero: "))
#         num2 = int(input("ingrese otro numero: "))
#         if num1 % num2 == 0 or num2 % num1 == 0:
#             print("alguno de los numeros es multiplo del otro.")
#             break
#         else:
#             print("intente nuevamente.")

# es_multiplo()

# def tabla_multiplicar():

#     while True:
#         multiplicador = 10
#         numero = int(input("ingrese un numero: "))
#         if numero > 0:
#             while multiplicador > 0:
#                 mostrar_numero = numero * multiplicador
#                 print(mostrar_numero)
#                 multiplicador -= 1
#         else:
#             print("a ingresado cero.")
#             break 
# tabla_multiplicar()

# def vocales():
#     palabra = input("Ingrese una palabra: ")
#     vocales = "aeiou"
#     contador_vocales = 0

#     for letra in palabra:
#         if letra in vocales:
#             contador_vocales += 1
#     else:
#         if contador_vocales == 0:
#             print("La palabra no contenia vocales.")
#         else:
#             print("la cantidad de vocales es ",contador_vocales)
# vocales()

# def lista_de_palabras():
#     palabras = input("Ingrese una lista de palabras: ").split()
#     for indice, palabra in enumerate(palabras):
#         print(f".{indice + 1}: {palabra}")
#         if palabra == "salir":
#             break
#         elif palabra == "omitir":
#             continue
#     else:
#         print("Ninguna palabra fue salir")

# lista_de_palabras()

# def inventario():
#     productos = input("Ingrese un producto: ")
#     cantidad = int(input("Ingrese la cantidad de este producto: "))
#     total_productos = 0
#     while productos != "salir":
#         print(f"el producto {productos} tiene un stock de {cantidad}")
#         total_productos += cantidad
#         productos = input("ingrese el nombre del producto o salir para salir: ")
#         cantidad = int(input("Ingrese la cantidad de este producto: "))
#     print("la cantidad total de articulos es: ", total_productos)
# inventario()

# ciudades_info = {
#     'Paris': {
#         'Pais': 'Francia',
#         'Poblacion': 2187526,
#         'Puntos_de_Interes': ['Torre Eiffel', 'Louvre', 'Catedral de Notre-Dame']
#     },
#     'Nueva York': {
#         'Pais': 'Estados Unidos',
#         'Poblacion': 8398748,
#         'Puntos_de_Interes': ['Estatua de la Libertad', 'Central Park', 'Times Square']
#     },
#     'Tokio': {
#         'Pais': 'Japón',
#         'Poblacion': 13929286,
#         'Puntos_de_Interes': ['Torre de Tokio', 'Templo Senso-ji', 'Palacio Imperial']
#     }
# }

# ciudad = input("ingrerse una de estas tres ciudades: ")

# try:
#     informacion = ciudades_info[ciudad]
#     print("Informacion sobre: ", ciudad)
#     print("Pais = ", informacion['Pais'])
#     print("Poblacion = ", informacion['Poblacion'])
#     print("Puntos de interes = ", informacion['Puntos_de_Interes'])
# except KeyError:
#     print("Ocurrio un error, la ciudad", ciudad, " no se encuentra en la base de datos.")

# try:
#     While edad != 0 :
#         edad = int(input("Ingrese su edad: "))

#     if edad <= 0:
#         raise ValueError()
#     else:
#         if edad > 18 and edad < 65:
#             print("A ingresado la edad correctamente, ", edad)
#             break
#     else:
#         int(input("ingrese una edad valida: "))

# except TypeError:
#     print("Error: la entrada no es un numero.")
# except ValueError:
#     print("Error: ingrese un numero valido.")
# except:
#     print("Error desconocido.")

# def compra():
#     try:
#         precio_producto = float(input("Ingrese el precio del producto: "))
#         codigo_descuento = (input("Ingrese el codigo de descuento: "))
        
#         if precio_producto <= 0:
#             raise ValueError("el precio debe ser un numero positivo.")
    
        
#         if precio_producto > 0:
#             if codigo_descuento == "DESC10":
#                 print("Tiene un 10% de descuento.")
#             elif codigo_descuento == "DESC20":
#                 print("TIene un 20% de descuento.")
#             elif codigo_descuento == "DESC30":
#                 print("Tiene un 30% de descuento.")
#             else:
#                 print("El codigo no es valido.")
#     except TypeError:
#         print("Error. La entrada no es valida.")
#     except ValueError as ve:
#         print(f"Error de valor: {ve}")
#     except Exception as e:
#         print(f"Error desconocido: {e}")

# compra()


# cancion = ""
# elefantes = 1
# limite = 5

# while elefantes <= limite:
#     print(elefantes, " elefante se balanceaba sobre la tela de una arania.")
#     elefantes += 1

# class Runners:
    
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def info(self):
#         print("Este es el print del metodo info de la clase Runners.")
        

# class Runner(Runners):

#     def __init__(self, nombre, edad, email):
#         super().__init__(nombre, edad)
#         self.email = email

#     def trabajo(self):
#         pass
    
#     def alimentacion(self):
#         pass

#     def deporte(self):
#         pass

#     def describirme(self):
#         print("soy el metodo [describirme]")

# mi_Persona = Runner("hector", 57, "hector@gmail.com")
# mi_Persona.describirme()

# class Figura():
#     def area(self):
#         pass

# class Circulo(Figura):
#     def __init__(self, radio):
#         self.radio = radio
    
#     def area(self):
#         return 3.1416 * self.radio * self.radio

# class Rectangulo(Figura):
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
    
#     def area(self):
#         return self.base * self.altura

# circulo = Circulo(5)
# rectangulo = Rectangulo(4, 5)
# print("El area del circulo es: ", circulo.area())
# print("El area del rectangulo es: ", rectangulo.area())

# class Calculadora():
    
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def suma(self):
#         return self.num1 + self.num2

# sumar = Calculadora(4, 5)
# print("la suma de dos numeros es", sumar.suma())

# class Calcu():
#     @classmethod
#     def suma(cls, num1, num2):
#         return num1 + num2
# resultado = Calcu.suma(5, 4)
# print("Resultado de la suma: ", resultado)

# class Empleado():

#     def __init__(self, nombre, apellido, edad, salario):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.salario = salario
    
#     def mostrar_informacion(self):
#         return f"Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}, Salario ${self.salario}"

#     def aumentar_salario(self, porcentaje):
#         self.salario += self.salario * (porcentaje/100)
    
# class Gerente(Empleado):

#     def __init__(self, nombre, apellido, edad, salario, departamento):
#         super().__init__(nombre, apellido, edad, salario)
#         self.departamento = departamento
    
#     def mostrar_informacion(self):
#         return super().mostrar_informacion() + f", Departamento: {self.departamento}"

# empleado = Empleado("Carlos", "Redondo", 44, 456147)
# gerente = Gerente("Osvaldo", "Gross", 67, 2000000, "Finanzas")

# print(empleado.mostrar_informacion())
# print(gerente.mostrar_informacion())

# empleado.aumentar_salario(20)
# print(f"El nuevo salario de {empleado.nombre} es: ${empleado.salario}")

# class Libro:

#     def __init__(self, titulo, autor, anio_publicacion):
#         self.titulo = titulo
#         self.autor = autor
#         self.anio_publicacion = anio_publicacion
#         self.disponible = True

# class Biblioteca:
    
#     cantidad_total_libros = 0

#     def __init__(self):
#         self.libros = []

#     def agregar_libros(self, libro):
#         self.libros.append(libro)
#         Biblioteca.cantidad_total_libros += 1
    
#     def prestar_libro(self, titulo):
#         for libro in self.libros:
#             if libro.titulo == titulo and libro.disponible:
#                 libro.disponible = False
#                 return f"El libro: '{titulo}' ha sido prestado."
#         return f"El libro: '{titulo}' no esta disponible."
    
#     def devolver_libro(self, titulo):
#         for libro in self.libros:
#             if libro.titulo == titulo and not libro.disponible:
#                 libro.disponible = True
#                 return f"El libro: '{titulo}' ha sido devuelto."
#         return f"El libro: '{titulo}' no puede ser devuelto."
    
#     def mostrar_libros_disponibles(self):
#         disponibles = [libro.titulo for libro in self.libros if libro.disponible]
#         return f"Libros disponibles: {','.join(disponibles)}"
    
# libro1 = Libro("Harry Potter", "J.K.Rowling", 2000)
# libro2 = Libro("Cien anios de soledad", "Gabriel Garcia Marquez", 1967)

# biblioteca = Biblioteca()
# biblioteca.agregar_libros(libro1)
# biblioteca.agregar_libros(libro2)

# print(biblioteca.prestar_libro("Harry Potter"))
# print(biblioteca.devolver_libro("Harry Potter"))
# print(biblioteca.mostrar_libros_disponibles)

class Producto():

    def __init__(self, nombre, precio, cantidad_disponible, codigo_producto):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.codigo_producto = codigo_producto

class CarritoCompras():
    cantidad_total_productos = 0
    
    def __init__(self):
        self.productos = []

    def agregar_productos(self, producto):
        self.productos.append(producto)
        CarritoCompras.cantidad_total_productos += 1
    
    def eliminar_productos(self, codigo_producto):
        for producto in self.productos:
            if producto.codigo_producto == codigo_producto:
                self.productos.remove(producto)
                CarritoCompras.cantidad_total_productos -= 1
                return f"Producto '{producto.nombre}' eliminado del carrito."
        return f"Producto con codigo '{codigo_producto}' no encontrado en el carrito."
    
    def calcular_total_compar(self):
        total = sum([producto.precio for producto in self.productos])
        return f"Total de la compra: ${total}"

producto1 = Producto("Laptop", 800, 5, "LP001")
producto2 = Producto("Telefono", 300, 10, "PH002")

carrito = CarritoCompras()
carrito.agregar_productos(producto1)
carrito.agregar_productos(producto2)

print(carrito.eliminar_productos("PH002"))
print(carrito.calcular_total_compar())
