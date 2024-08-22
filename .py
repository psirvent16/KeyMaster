def leer_nums():
    numeros = []
    numero = 0

    while numero != -1:
        numero = int(input("Ingrese un número entero o -1 para finalizar): "))
        
        if numero != -1:
            repetido = False
            i = 0
            while i < len(numeros):
                if numeros[i] == numero:
                    repetido = True
                    break
                i += 1
            
            if repetido:
                print("Ingrese un número diferente")
            else:
                numeros.append(numero)
    
    return numeros

def burbujeo(numeros):
    n = len(numeros)
    i = 0
    while i < n:
        intercambio = False
        k = 0
        while k < n - i - 1:
            if numeros[k] > numeros[k + 1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                numeros[k], numeros[k + 1] = numeros[k + 1], numeros[k]
                intercambio = True
            k += 1
        if not intercambio:
            break
        i += 1

def calcular_promedio(numeros):
    if len(numeros) <= 2:
        print("Debe haber mínimo un número para calcular el promedio al descartar el mínimo y el máximo.")
        return
    
    # Ordenar la lista usando el método de burbujeo
    burbujeo(numeros)
    
    minimo = numeros[0]
    maximo = numeros[-1]
    
    # Crear una nueva lista sin el mínimo y el máximo
    numeros_medio = []
    i = 0
    while i < len(numeros):
        if numeros[i] != minimo and numeros[i] != maximo:
            numeros_medio.append(numeros[i])
        i += 1
    
    if len(numeros_medio) == 0:
        print("No hay más números al eliminar el mínimo y el máximo.")
        return
    
    suma = 0
    i = 0
    while i < len(numeros_medio):
        suma += numeros_medio[i]
        i += 1
    
    promedio = suma / len(numeros_medio)
    
    print("El promedio de los números del medio es:", promedio)

def main():
    numeros = leer_nums()
    calcular_promedio(numeros)

main()
