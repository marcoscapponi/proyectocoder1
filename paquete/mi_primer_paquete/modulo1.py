# class Persona:

#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido
    
#     def __str__(self):
#         return f"Nombre {self.nombre}"
    

class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre 
        self.nota = nota

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nNota: {self.nota}"

def imprimir():
    print("funciono a la perfeccion.")

imprimir()