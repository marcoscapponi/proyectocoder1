print(10+5)
print(10-5)
print(10/5)
print(10*5)
print(5**3) ## potencia
print(10%5) ## resto de la division
print(20//3) ## cociente de la division

###################################################################

#altura = float(input("ingrese la altura del rectangulo: ",))
#base = float(input("ingrese la base del rectangulo: ", ))
#area = altura * base
#print("el are del rectangulo es: ", area)

#base_triangulo = float(input("ingrese la base del triangulo: ",))
#altura_triangulo = float(input("ingrese la altura del triangulo: ", ))
#area_triangulo = (base_triangulo * altura_triangulo)/2
#print("el area del triangulo es : ", area_triangulo)





soleado = True
lluvioso = False
dia = lluvioso

print("es un dia soleado?", dia == lluvioso)
print("el valor de dia es = ", dia)


expresio0nes = [not True == False, False == True, 10 >= 2*4, 33/3 == 11, True > False, True*5 == 2.5*2]
print(expresio0nes)

expresiones = [not False, not 3 == 5, 33/3 == 11 and 5 > 2, True or False, True * 5 == 2.5 * 2 or 123 >= 23, 12 > 7 and True < False]
print(expresiones)

a = 15
b = 12
carlin = a**b/3**a/a*b >=15 and not (a%b**2)!=0
print(carlin)

NOMBRE = str(input("ingrese el nombre: ", ))
EDAD = int(input("ingrese la edad: ", ))

Variables = [NOMBRE != "****", EDAD >= 4 and EDAD < 8, EDAD * 3 > 35]

print(Variables)






