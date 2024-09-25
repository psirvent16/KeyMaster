import random
import string

# Lista de usuarios, cada usuario será una lista con su nombre y contraseña cifrada
usuarios = []

# Función para agregar un usuario
def agregar_usuario(nombre, contrasena):
    # Cifrado simple: cifrado César con desplazamiento de 3
    contrasena_cifrada = ''.join(map(lambda x: chr((ord(x) + 3) % 126), contrasena))
    usuarios.append([nombre, contrasena_cifrada])
    print(f"Usuario {nombre} agregado correctamente.")

# Generar una contraseña segura
def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

# Función para validar que una contraseña sea segura (mínimo 8 caracteres, al menos una mayúscula, minúscula y número)
def validar_contrasena(contrasena):
    if (len(contrasena) >= 8 and 
        any(c.islower() for c in contrasena) and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena)):
        return True
    return False

# Función para eliminar usuario
def eliminar_usuario(nombre):
    global usuarios
    usuarios = list(filter(lambda x: x[0] != nombre, usuarios))
    print(f"Usuario {nombre} eliminado correctamente.")

# Ejemplo de uso
nueva_contrasena = generar_contrasena()
print(f"Contraseña generada: {nueva_contrasena}")

if validar_contrasena(nueva_contrasena):
    agregar_usuario("usuario1", nueva_contrasena)
else:
    print("La contraseña no es segura.")
