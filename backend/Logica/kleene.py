def kleene_star(L, max_iter):
    # Basado en el Algoritmo KleeneStar [cite: 95, 96]
    # Representa L* (cero o más repeticiones) [cite: 93]
    resultado = [""]  # Incluye cadena vacía (lambda)
    actual = [""]
    
    for i in range(1, max_iter + 1):
        nuevo = []
        for x in actual:
            for y in L:
                cadena = x + y
                if cadena not in nuevo:
                    nuevo.append(cadena)
        
        # Agregar a resultado si no está [cite: 96]
        for elemento in nuevo:
            if elemento not in resultado:
                resultado.append(elemento)
        actual = nuevo
    return resultado

def kleene_plus(L, max_iter):
    # Basado en el Algoritmo KleenePlus [cite: 105]
    ks = kleene_star(L, max_iter)
    # Retorna ks sin la cadena vacía (lambda) [cite: 103, 110]
    return [elemento for elemento in ks if elemento != ""]