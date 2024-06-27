nombre = print(input("como te llamas? ", ))
preferencia = (input("Cual es tu preferencia (M o C)? ",))

if preferencia == "M":
    print("Tu grupo es B")
else:
    print("Tu grupo es A")

a = 25
b =50
if b > a:
    print("b es mas grande que a")


## generaciones digitales

anio = 2000
if anio >= 1920 and anio < 1940:
    print("Generacion Z")
elif anio > 1946 and anio < 1964:
    print("Baby Boomer")
elif anio > 1965 and anio < 1979:
    print("Generacion X")
elif anio > 1980 and anio <= 2000:
    print("Generacion Y")
elif anio > 2001 and anio < 2010:
    print("Generacion Z")
else:
    print ("No existe generacion asociada")


edad = 15
antiguedad = 10
ingreso = 5500

if edad > 18 and antiguedad > 3 and ingreso > 2500:
    print("credito aprobado")
elif edad < 18 and ingreso > 4000:
    print("credito aprobado")
else:
    print ("no se aprueba el credito")