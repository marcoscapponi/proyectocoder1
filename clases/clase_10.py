def dividir(a,b):
    if b == 0:
        return None
    return a/b
print(dividir(10,5))
print(dividir(10,0))

while (True):
    try:
        a = float(input("introduce un numero: "))
        b = float(input("introduce otro numero: "))
        print(a + b)
    except:
        print("ha ocurrido un error. Tienes que introducir 2 numeros.")
    else:
        print("la suma se ha realizado correctamente")
        break
    finally:
        print("fin del bucle")
    
try:
    n = float(input("introduce un numero divisor: "))
    5/n
except TypeError:
    print("no se puede dividir el numero entre cadena")
except ValueError:
    print("debes introducir una cadena que sea un numero")
except ZeroDivisionError:
    print("no se puede dividir por cero, prueba otro numero")
except Exception as e:
    print("ha ocurrido un error no previsto", type(e).__name__)

try:
    m = input("introduce un numero: ")
    5/m
except Exception as e:
    print("ha ocurrido un error =>", type(e).__name__)

print(type(1))
print(type(3.14))
print(type([]))
print(type(()))
#print(type(e).__name__)
print(type(1).__name__)
print(type(3.14).__name__)
print(type([]).__name__)
print(type(()).__name__)



def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return None
