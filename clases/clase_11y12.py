# class Perro:
    
#     especie = "Mamifero"

#     def __init__(self, nombre, raza):
#         self.nombre = nombre
#         self.raza = raza
#     def __str__(self):
#         return "nombre:" +self.nombre +", Raza:" +self.raza +", Especie:" +self.especie
#     def ladrar(self):
#         print("Este perro ha ladrado :( \nEsta enojado") 
#     def caminar(self, pasos):
#         print(f"Este perro ha caminado {pasos} pasos")

# class Persona:
#     def __init__(self, nombre, apellido, perro):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.perro = perro
#     def __Str__(self):
#         return "Mi nombre es: " +self.nombre +" " +self.apellido +"\n" +self.perro.__str__()
    

# mi_perro = Perro("Toby", "Bull dog")
# mi_persona = Persona("Nicolas", "Perez", mi_perro)

# print(mi_persona)

# class Vector():
#     def __init__(self, data):
#         self._data = data
#     def __str__(self):
#         return f"The values are: {self._data}"
#     def __len__(self):
#         return len(self._data)
#     def __getitem__(self, pos):
#         return self._data[pos]
#     def __setitem__(self, pos, value):
#         self._data[pos] = value
#     def __iter__(self):
#         for pos in range(0, len(self._data)):
#             yield f"Value[{pos}]: {self._data[pos]}"
# v = Vector([1, 2])
# for vec in v:
#     print(vec)

# class Sueldo:

#     def __init__(self, sueldo):
#         self.sueldo = sueldo
#     def __str__(self):
#         return f"\nSUELDO: {self.sueldo}"
    
    
#     class Empleado:

#         def __init__(self, nombre, puesto):
#             self.nombre = nombre
#             self.puesto = puesto
#             self.sueldo = Sueldo(1200)

#         def __str__(self):
#             return f"NOMBRE: {self.nombre}\nPUESTO: {self.puesto}\n" +self.sueldo.__str__()
# s1 = Sueldo(200)
# emp1 = Sueldo.Empleado("Nico", "Profe")

# print("RESULTADO 1: " +s1.__str__())
# print("RESULTADO 2: " +emp1.__str__())

# class Persona:

#     tipo = "Humano"
#     __sueldo = 2000

#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.__apellido = apellido

#     def __soy_feliz(self):
#         print("no les importa __")
    
#     def edad(self):
#         return 31 

# persona1 = Persona("Nicolas", "Lopez")

# print(f"Resultado1: {persona1.tipo}\n")
# print(f"Resultado2: {persona1.__sueldo}\n")
# print(f"Resultado3: {persona1.nombre}\n")
# print(f"Resultado4: {persona1.__apellido}\n")
# print(f"Resultado5: {persona1.__soy_feliz()}\n")
# print(f"Resultado6: {persona1.edad()}\n")


class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return f"NOMBRE: {self.nombre}\nPUESTO: {self.nota}" 

    def Aprobo(self):
        if self.nota > "5":
            print("Aprobo")
        else:
            print("Desaprobo")


alumn = Alumno("Marcos", "4")

print(alumn)
print(alumn.Aprobo())