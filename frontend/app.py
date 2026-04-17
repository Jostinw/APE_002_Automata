import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Teoría de Autómatas - APE 2", layout="wide")

st.title("🛠️ Analizador de Estructuras Formales")
st.markdown("---")

# URL del Backend corregida al puerto 8050
URL_BASE = "http://127.0.0.1:8050"

# Sidebar para configuración global
with st.sidebar:
    st.header("⚙️ Configuración")
    # Alfabetos sugeridos por la práctica: "0,1" (Binario), "a,b,c" (Letras), "1,2,3" (Números)
    alfabeto_input = st.text_input("Definir Alfabeto (separado por comas)", "0,1")
    alfabeto = [s.strip() for s in alfabeto_input.split(",")]
    
    # Se quitó el texto "(Kleene)" como solicitaste
    max_iter = st.slider("Máximo de iteraciones", 1, 20, 3)

# División en pestañas según la guía
tab1, tab2, tab3 = st.tabs(["Generación y Pertenencia", "Operaciones de Lenguajes", "Crecimiento"])

# --- TAB 1: GENERACIÓN ---
with tab1:
    st.header("1. Generación de Cadenas")
    st.info("Prueba con alfabetos como: '0,1' (Binario), 'a,b' (Letras) o '+,*,-' (Símbolos)")
    n = st.number_input("Longitud máxima (n)", min_value=1, max_value=20, value=2)
    
    if st.button("Generar Cadenas"):
        try:
            payload = {"alfabeto": alfabeto, "max_len": n}
            response = requests.post(f"{URL_BASE}/generar", json=payload)
            
            if response.status_code == 200:
                cadenas = response.json()["resultado"]
                st.success(f" Se generaron {len(cadenas)} cadenas (incluida λ):")
                st.write(cadenas)
                
                # Guardar en estado de sesión para la prueba de pertenencia
                st.session_state['cadenas_generadas'] = cadenas
            else:
                st.error(f"Error en el servidor: {response.status_code}")
        except Exception as e:
            st.error(f" Error de conexión: {e}. Asegúrate de que el backend corra en el puerto 8050.")

    st.markdown("---")
    st.subheader("2. Verificar Pertenencia")
    test_cadena = st.text_input("Ingresa una cadena para verificar")
    if st.button("¿Pertenece?"):
        if 'cadenas_generadas' in st.session_state:
            if test_cadena in st.session_state['cadenas_generadas']:
                st.info(f"La cadena '{test_cadena}' PERTENECE al lenguaje generado.")
            else:
                st.warning(f"La cadena '{test_cadena}' NO PERTENECE.")
        else:
            st.error("Primero debes generar las cadenas en el botón de arriba.")

# --- TAB 2: OPERACIONES ---
with tab2:
    st.header("3. Unión, Concatenación y Clausura")
    col1, col2 = st.columns(2)
    with col1:
        l1_input = st.text_input("Lenguaje L1 (ej: 0, 00)", "0,1")
        L1 = [s.strip() for s in l1_input.split(",")]
    with col2:
        l2_input = st.text_input("Lenguaje L2 (ej: 1, 11)", "a,b")
        L2 = [s.strip() for s in l2_input.split(",")]

    if st.button("Ejecutar Operaciones"):
        try:
            payload = {"L1": L1, "L2": L2, "max_iter": max_iter}
            response = requests.post(f"{URL_BASE}/operaciones", json=payload)
            
            if response.status_code == 200:
                res = response.json()
                st.subheader("Unión (L1 ∪ L2)")
                st.write(res["union"])
                
                st.subheader("Concatenación (L1 · L2)")
                st.write(res["concatenacion"])
                
                st.subheader(f"Clausura de Estrella (L1*) - {max_iter} iteraciones")
                st.write(res["kleene_star"])
                
                # Asegúrate de tener este endpoint definido en tu backend
                if "kleene_plus" in res:
                    st.subheader(f"Clausura Positiva (L1+) - {max_iter} iteraciones")
                    st.write(res["kleene_plus"])
            else:
                st.error(f"Error del servidor: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")

# --- TAB 3: CRECIMIENTO ---
with tab3:
    st.header("4. Análisis de Crecimiento")
    st.info("Este análisis ejecuta la generación desde 1 hasta 5 iteraciones para L1.")
    
    if st.button("Calcular Crecimiento"):
        try:
            response = requests.post(f"{URL_BASE}/analizar-crecimiento", json={"L1": L1})
            if response.status_code == 200:
                reporte = response.json()["reporte"]
                st.table(reporte)
                
                datos_grafica = {item['iteracion']: item['cantidad'] for item in reporte}
                st.line_chart(datos_grafica)
                st.caption("Gráfico de crecimiento exponencial de las cadenas.")
        except Exception as e:
            st.error(f"Error al conectar: {e}")