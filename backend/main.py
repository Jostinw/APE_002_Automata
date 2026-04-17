from fastapi import FastAPI
from pydantic import BaseModel
from Logica.strings import generar_cadenas
from Logica.operations import union, concatenacion
from Logica.kleene import kleene_star, kleene_plus

app = FastAPI()

class LanguageData(BaseModel):
    alfabeto: list = []
    max_len: int = 0
    L1: list = []
    L2: list = []
    max_iter: int = 3

@app.post("/generar")
def api_generar(data: LanguageData):
    res = generar_cadenas(data.alfabeto, data.max_len)
    return {"resultado": res}

@app.post("/operaciones")
def api_operaciones(data: LanguageData):
    try:
        # Asegúrate de importar estas funciones de tus archivos de Logica
        res_union = union(data.L1, data.L2)
        res_concat = concatenacion(data.L1, data.L2)
        res_star = kleene_star(data.L1, data.max_iter)
        res_plus = kleene_plus(data.L1, data.max_iter) # Agregado para cumplir con Algoritmo 6 [cite: 105]

        return {
            "union": res_union,
            "concatenacion": res_concat,
            "kleene_star": res_star,
            "kleene_plus": res_plus
        }
    except Exception as e:
        print(f"Error interno: {e}")
        return {"error": str(e)}
        
@app.post("/analizar-crecimiento")
def api_analizar_crecimiento(data: LanguageData):
    reporte = []
    # Cambiamos el rango para que use el max_iter enviado o un límite mayor
    for i in range(1, 21): 
        res = kleene_star(data.L1, i)
        reporte.append({"iteracion": i, "cantidad": len(res)})
    return {"reporte": reporte}