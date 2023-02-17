def cuadrado_y_grupo(matrix):
    cuadrado_latino(matrix)
    grupo(matrix)

def grupo(matrix):
     # se verifica si se cumple el cierre
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            concatenacion = matrix[i] + matrix[j]
            if concatenacion not in matrix:
                print('no cumple la propiedad de cierre')
                return False
    
    # se verifica si se cumple si es asociativa
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                concatenacion1 = matrix[i] + matrix[j] + matrix[k]
                concatenacion2 = matrix[i] + (matrix[j] + matrix[k])
                if concatenacion1 != concatenacion2:
                    print('no cumple la propiedad de asociatividad')
                    return False
    
    # Verifica si se cumple la identidad
    identidad = None
    for i in range(len(matrix)):
        tiene_identidad = all(matrix[j] + matrix[i] == matrix[j] for j in range(len(matrix)))
        if tiene_identidad:
            identidad = matrix[i]
            break
    if identidad is None:
        print('no cumple la propiedad identidad')
        return False
    
    # Verificar inverso
    for i in range(len(matrix)):
        tiene_inverso = False
        for j in range(len(matrix)):
            if matrix[i] + matrix[j] == identidad and matrix[j] + matrix[i] == identidad:
                tiene_inverso = True
                break
        if not tiene_inverso:
            print('no cumple la propiedad inverso')
            return False
    print(f'la matrix es un grupo {matrix}')
    return

def cuadrado_latino(matrix):
    #con el ciclo for se revisa que no haya elementos repetidos comparando el set creado a la longitud de la fila
    for fila in matrix:
        fila_set = set(fila)
        if len(fila) != len(fila_set):
            print(f'hay elementos que se repiten dentro de la fila {fila}')
            return False

    primera_fila=set(matrix[0])
    #se compara el set de la primera fila con las demas, para comprobar que las demas filas tengan los elementos
    for fila in matrix:
        fila_set=set(fila)
        #si el 
        if fila_set != primera_fila :
            print(f'no es un cuadrado latino ya que hay elementos que no coinciden {fila_set} y {primera_fila}')
            return False

    print(f'la matrix dada es un cuadrado latino: {matrix}')
    return True

# tamaño de la matrix
n = int(input("Ingresa el tamaño de la matrix: "))

# matrix vacia nxn
matrix = []
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(0)
    matrix.append(fila)

# Ingresar los elementos de la matrix
for i in range(n):
    for j in range(n):
        valor = input(f"Ingrese el valor de la posición [{i},{j}]: ")
        matrix[i][j] = valor

cuadrado_y_grupo(matrix)