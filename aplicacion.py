def leer_producto():
    with open("nombre.txt", "rt", encoding='utf8') as nombre_file:
        datos_nombre = nombre_file.read()
        
    with open("codigo.txt", "rt", encoding='utf8') as codigo_file:
        datos_codigo = codigo_file.read()
        
    with open("precio.txt", "rt", encoding='utf8') as precio_file:
        datos_precio = precio_file.read()
        
    return datos_nombre, datos_codigo, datos_precio

def agregar_producto(nombre_content, codigo_content, precio_content):
    with open("nombre.txt", "at", encoding='utf8') as nombre_file:
        nombre_file.write(nombre_content)
        
    with open("codigo.txt", "at", encoding='utf8') as codigo_file:
        codigo_file.write(codigo_content)
        
    with open("precio.txt", "at", encoding='utf8') as precio_file:
        precio_file.write(precio_content)

def menu():
    print("MENU PRINCIPAL")
    print("1. Listar productos")
    print("2. Agregar productos")
    print("3. Salir")
    
def listar():
    with open("nombre.txt", "r") as nombre, open("codigo.txt", "r") as codigo, open("precio.txt", "r") as precio:
        for nombre, codigo, precio in zip(nombre, codigo, precio):
            print(f"Nombre: {nombre.strip()} - Codigos: {codigo.strip()} - Precios: {precio.strip()}")



def agregar():
    nombre_content = input("Ingrese nombre: ")
    codigo_content = input("Ingrese codigo: ")
    precio_content = input("Ingrese precio: ")
    agregar_producto("\n" + nombre_content,"\n" + codigo_content ,"\n" + precio_content)
    print("Producto agregado con éxito.")


def salir():
    print("Gracias por su visita....")

def error():
    print("Opción incorrecta")

login = open("usuarios.txt","rt")
leerLogin = login.read().strip()
password = open("claves.txt","rt")
leerPassword = password.read().strip()
intentos = 0
while intentos < 3:
    user = input("Ingrese su usuario: ")
    clave = input("Ingrese la clave: ")
    if user == leerLogin and clave == leerPassword:
        opcion = 1
        while True:
            menu()
            opcion = int(input("\nopcion: "))
            if opcion == 1:
                listar()
            elif opcion == 2:
                agregar()
            elif opcion == 3:
                salir()
                break
            else:
                error()
        break  # Salir del bucle si las credenciales son correctas
    else:
        print("El usuario y/o clave es incorrecto")
        intentos += 1
        if intentos == 3:
            print("Número máximo de intentos alcanzado. Saliendo del programa.")
            break