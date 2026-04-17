def generar_cadenas(alfabeto, max_len):
    # Basado en el Algoritmo GenerarCadenas [cite: 32, 51]
    resultado = [""] # Representa lambda (λ) [cite: 34]
    for i in range(1, max_len + 1):
        nuevas = []
        for cadena in resultado:
            for simbolo in alfabeto:
                nuevas.append(cadena + simbolo)
        resultado.extend(nuevas)
    return list(set(resultado)) # Eliminar duplicados [cite: 42, 50]

def pertenece(cadena, lenguaje):
    # Basado en el Algoritmo Pertenece [cite: 60, 66]
    return cadena in lenguaje