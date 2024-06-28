def registro_usuario(usuarios, nombre_usuario, contrasenia):
    if nombre_usuario in usuarios:
        print("El usuario ya existe.")
    else:
        usuarios[nombre_usuario] = contrasenia
        print("Usuario registrado con exito.")

def mostrar_usuarios(usuarios):
    print("Usuarios registrados: ")
    for usuario in usuarios:
        print(".", usuario)

def login_usuario(usuarios, nombre_usuario, contrasenia):
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasenia:
        print("bienvenido ", nombre_usuario, ".")
    else:
        print("ERROR, nombre de usuario o contrasenia incorrecta.")

usuarios = {}

def funcion_principal():
    while True:
        print("Menu\n")
        print("1. Login in ")
        print("2. Mostrar usuarios registrados")
        print("3. Registrarse")
        print("4. Salir")

        elegir = input("Seleccione una opcion: ")

        if elegir == '1':
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            contrasenia = input("Ingrese su contrasenia: ")
            login_usuario(usuarios, nombre_usuario, contrasenia)
        elif elegir == '2':
            mostrar_usuarios(usuarios)
        elif elegir == '3':
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            contrasenia =  input("Ingrese la contrasenia: ")
            registro_usuario(usuarios, nombre_usuario, contrasenia)
        elif elegir == '4':
            print("Gracias, hasta la proxima.")
            break
        else:
            print("Error. Opcion no valida")

funcion_principal()
