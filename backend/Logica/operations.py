def union(L1, L2):
    # Basado en el Algoritmo Union [cite: 71, 80]
    resultado = list(L1)  # Copia de L1 [cite: 73]
    for elemento in L2:
        if elemento not in resultado:  # Sin repetir elementos [cite: 69, 75]
            resultado.append(elemento)
    return resultado

def concatenacion(L1, L2):
    # Basado en el Algoritmo Concatenacion [cite: 90]
    resultado = []
    for x in L1:
        for y in L2:
            resultado.append(x + y)  # nueva x + y [cite: 90]
    return resultado