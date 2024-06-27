# num = 5
# while num > 0:
#     print(f'{num}')
#     num -= 1
# print("termino el conteo")



# n = 0
# while n <= 5:
#     n += 1
#     print('N vale', n)

# chance = 1
# while chance <= 3:
#     txt = input("escribe SI: ")
#     if txt == "SI":
#         print("ok, lo conseguiste en el intento: ", chance)
#         break
#     chance += 1
# else:
#     print("has agotado tus tres intentos")



# num = int(input("ingrese un numero: "))
# while num != 0:
#     print(num)
#     otro_num = input("ingrese otro numero o 'exit' para salir: ")
    
#     if otro_num == 'exit':
#         print("a salido del programa")
#         break
    
#     num = int(num) + int(otro_num)


# i = 0
# while i < 6:
#  i +=1
#  if i == 3:
#     continue
#  print(i) 

# j = 0
# while j < 10:
#     j+=1
#     if j == 2:
#         pass
#         print('n vale', j)

# k = -3
# while k < 10:
#     k+=1
#     if k == 2:
#         continue
#     print('n vale', k)


# numeros = [0,1,2,3,4,5,6,7,8,9,10]
# for indice, numero in enumerate(numeros):
#     numeros[indice]*=5
#     print(numero)
#     print(numeros)

# for olga in range(10):
#  if olga == 2:
#     continue
#  elif olga == 8:
#      break
#  else:
#      print("se termino de iterar y numero vale: ", olga)

# colores = ['rojo', 'verde', 'azul', 'amarillo']
# for indice, coloe in enumerate(colores):
#     print(f"el color en la posicion {indice} es {coloe}")

# lista = [1, 2, 3, 4, 5]
# for valor in lista:
#     print("Soy un item de la lista y valgo ", valor)

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in lista:
#     print("Soy un valor de la lista y valgo ", num)
#     num *= 5
#     print("Soy un valor de la lista y ahora valgo", num)

# indice = 0
# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for numero in numeros:
#     numeros[indice] *= 5
#     indice += 1
# print(numeros)


# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for indice, numero in enumerate(numeros):
#     numeros[indice] *= 5
# print(numeros)

texto = "Hola mundo, estoy usando python"
for letra in texto:
    print (letra)
texto2 = ""
for letra in texto:
    texto2 = letra * 2
print(texto2)