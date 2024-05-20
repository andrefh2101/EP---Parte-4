login = open("usuarios.txt","rt")
leerLogin = login.read().strip()
password = open("claves.txt","rt")
leerPassword = password.read().strip()
intentos = 0
while intentos < 3:
    user = input("Ingrese su usuario: ")
    clave = input("Ingrese la clave: ")
    if user == leerLogin and clave == leerPassword:
        print("Datos Producto:")
        print("1. Listar")
        print("2. Agregar")
        print("3. Salir")
        break  # Salir del bucle si las credenciales son correctas
    else:
        print("El usuario y/o clave es incorrecto")
        intentos += 1
        if intentos == 3:
            print("Número máximo de intentos alcanzado. Saliendo del programa.")
            break