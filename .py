import random
import string

usuarios_registrados = {}

def generar_contraseña(longitud=12):
    
    
    caracteres_disponibles = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres_disponibles) for _ in range(longitud))
    return contraseña
  
  #Paso 2


def registrar_usuario(nombre):
   
    if nombre in usuarios_registrados:
        print(f"El usuario {nombre} ya está registrado.")
        return
    
    
    nueva_contraseña = generar_contraseña()
    usuarios_registrados[nombre] = (nombre, nueva_contraseña)
    print(f"Usuario {nombre} registrado correctamente con la contraseña: {nueva_contraseña}")


    #Paso 3


def mostrar_usuarios():
   
    if usuarios_registrados:
        print("Lista de usuarios registrados:")
        for usuario, (nombre, contraseña) in usuarios_registrados.items():
            print(f"Usuario: {nombre}, Contraseña: {contraseña}")
    else:
        print("No hay usuarios registrados.")




   #Paso 4

def contar_usuarios():
    
    total = len(usuarios_registrados)
    print(f"Total de usuarios registrados: {total}")
    return total


#Paso 5


def validar_contraseña(contraseña):
    
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    if not any(c.isdigit() for c in contraseña):
        print("La contraseña debe contener al menos un número.")
        return False
    if not any(c.isalpha() for c in contraseña):
        print("La contraseña debe contener al menos una letra.")
        return False
    if not any(c in string.punctuation for c in contraseña):
        print("La contraseña debe contener al menos un símbolo.")
        return False
    return True
  #PASO 6


def mostrar_info_usuario(nombre):
  
    if nombre in usuarios_registrados:
        _, contraseña = usuarios_registrados[nombre]
        print(f"Información del usuario {nombre}:")
        print(f"Contraseña: {contraseña}")
    else:
        print(f"Usuario {nombre} no encontrado.")


        #PASO 7
        


def main():
    
    
    while True:
        print("\nMenú de opciones:")
        print("1. Registrar un nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Contar usuarios registrados")
        print("4. Validar una contraseña")
        print("5. Mostrar información de un usuario")
        print("6. Salir del programa")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre_usuario = input("Introduce el nombre del usuario: ")
            registrar_usuario(nombre_usuario)
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            contar_usuarios()
        elif opcion == "4":
            contraseña_usuario = input("Introduce la contraseña para validar: ")
            if validar_contraseña(contraseña_usuario):
                print("Contraseña válida.")
            else:
                print("Contraseña no válida.")
        elif opcion == "5":
            nombre_usuario = input("Introduce el nombre del usuario: ")
            mostrar_info_usuario(nombre_usuario)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()


 