import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Tesina - Límite de una función", layout="wide")
st.sidebar.title("Tesina")
unidad = st.sidebar.radio("Elegí la unidad:", ["Unidad 0 - Introducción", "Unidad 1 - Límite de una función"])

if unidad == "Unidad 0 - Introducción":
    st.title("Visualizador del Límite")
    st.latex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1")
    x = st.slider("Mover x hacia 0", -3.0, 3.0, 1.5)
    def f(v):
        return 1.0 if abs(v) < 0.0001 else np.sin(v)/v
    xs = np.linspace(-3, 3, 500)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=[f(i) for i in xs], mode="lines", name="f(x) = sin(x)/x"))
    fig.add_trace(go.Scatter(x=[x], y=[f(x)], mode="markers", marker=dict(size=12, color="red"), name="Punto actual"))
    fig.add_hline(y=1, line_dash="dash")
    fig.update_layout(xaxis_title="x", yaxis_title="f(x)")
    st.plotly_chart(fig, use_container_width=True)
    st.metric("f(x)", f"{f(x):.5f}")
    if abs(x) > 1:
        st.warning("Acercate a 0...")
    else:
        st.success("Converge a 1")

elif unidad == "Unidad 1 - Límite de una función":
    st.title("Unidad 1 - Límite de una función")
    st.caption("Fuente: Stewart, James (1998). Cálculo de una variable.")
    st.header("(1) DEFINICIÓN - Límite")
    st.latex(r"\lim_{x \to a} f(x) = L")
    st.write("Se dice: **el límite de f(x) es igual a L cuando x tiende a a** si podemos acercar arbitrariamente los valores de f(x) a L (tanto como queramos) aproximando x a a, pero **sin igualar a a**.")
    st.info("Esto significa que los valores de f(x) se acercan más y más al número L conforme x se aproxima al número a (de ambos lados de a), pero x ≠ a.")
    st.write("Notación alternativa:")
    st.latex(r"f(x) \to L \quad \text{cuando} \quad x \to a")
    st.warning("Hay que subrayar la frase **'pero x ≠ a'**. En la búsqueda del límite, nunca consideramos x = a. f(x) ni siquiera necesita estar definida cuando x = a. Lo único que interesa es cómo se define f cerca de a.")
    st.subheader("Ejemplo de la Definición (1)")
    st.write("Investiguemos la función:")
    st.latex(r"f(x) = x^2 - x + 2")
    st.write("cuando x se acerca a 2, pero sin ser igual a 2.")
    st.table(pd.DataFrame({
        "x (por izquierda)": [1.0, 1.5, 1.8, 1.9, 1.95, 1.99, 1.995, 1.999],
        "f(x)": [2.0, 2.75, 3.44, 3.71, 3.8525, 3.9701, 3.9850, 3.9970],
        "x (por derecha)": [3.0, 2.5, 2.2, 2.1, 2.05, 2.01, 2.005, 2.001],
        "f(x)": [8.0, 5.75, 4.64, 4.31, 4.1525, 4.0301, 4.0150, 4.0030]
    }))
    st.latex(r"\lim_{x \to 2} (x^2 - x + 2) = 4")
    x1 = st.slider("Mover x hacia 2 - Ejemplo f(x)=x²-x+2", 0.0, 4.0, 1.5)
    def f1(v): return v
             xs = np.linspace(0, 4, 400)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=[f1(i) for i in xs], mode="lines", name="y = x² - x + 2"))
    fig.add_trace(go.Scatter(x=[x1], y=[f1(x1)], mode="markers", marker=dict(size=13, color="red"), name="Punto actual"))
    fig.add_trace(go.Scatter(x=[2], y=[4], mode="markers", marker=dict(size=12, color="green"), name="Límite = 4"))
    fig.add_hline(y=4, line_dash="dash")
    fig.add_vline(x=2, line_dash="dash")
    fig.update_layout(xaxis_title="x", yaxis_title="f(x)")
    st.plotly_chart(fig, use_container_width=True)
    st.metric("f(x)", f"{f1(x1):.4f}")
    st.caption("Figura 1 del libro: la parábola tiende a 4.")
    st.write("**Figura 2 del libro:** En los tres casos a), b) y c), aunque f(a) no esté definida o f(a) ≠ L, en cada caso se cumple:")
    st.latex(r"\lim_{x \to a} f(x) = L")
    st.write("Lo que pasa EN a no importa. Importa lo que pasa CERCA de a.")   st.header("(2) y (3) DEFINICIÓN - Límites laterales")
    st.subheader("Límite por la izquierda")
    st.latex(r"\lim_{x \to a^{-}} f(x) = L")
    st.write("Se dice que el límite lateral izquierdo de f(x) cuando x tiende a a es igual a L si podemos acercar arbitrariamente los valores de f(x) a L por la izquierda, aproximando x a a, con x menor que a.")
    st.write("El símbolo **x → a⁻** indica que sólo se consideran valores de x menores que a.")
    st.subheader("Límite por la derecha")
    st.latex(r"\lim_{x \to a^{+}} f(x) = L")
    st.write("De igual forma, si precisamos que x sea mayor que a, obtenemos el límite lateral derecho.")
    st.write("El símbolo **x → a⁺** indica que sólo se consideran valores de x mayores que a.")
    st.success("Regla clave (3): El límite existe si y sólo si los dos laterales son iguales:")
    st.latex(r"\lim_{x \to a} f(x) = L \iff \lim_{x \to a^{-}} f(x) = L \quad y \quad \lim_{x \to a^{+}} f(x) = L")
    st.subheader("Ejemplo gráfico - Límites laterales")
    st.latex(r"\lim_{x \to 0^{-}} H(x) = 0 \quad y \quad \lim_{x \to 0^{+}} H(x) = 1")
    st.write("En este ejemplo los laterales NO son iguales, entonces el límite general NO existe.")
    st.header("(4) DEFINICIÓN - Límite infinito +∞")
    st.latex(r"\lim_{x \to a} f(x) = \infty")
    st.write("Significa que los valores de f(x) se pueden incrementar arbitrariamente, tanto como queramos, acercando x lo suficiente a a (pero sin igualarla con a).")
    st.latex(r"f(x) \to \infty \quad \text{cuando} \quad x \to a")
    st.warning("El símbolo ∞ NO es un número. Solo expresa el modo particular en que NO existe el límite.")
    st.subheader("Ejemplo: 1/x²")
    st.latex(r"\lim_{x \to 0} \frac{1}{x^2} = \infty")
    x4 = st.slider("Mover x hacia 0 - Ejemplo 1/x²", -1.0, 1.0, 0.5)
    def f4(v): return 100 if abs(v) < 0.05 else 1/(v**2)
    xs4 = np.linspace(-1, 1, 500)
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=xs4, y=[min(f4(i), 50) for i in xs4], mode="lines", name="y = 1/x²"))
    fig4.add_trace(go.Scatter(x=[x4], y=[min(f4(x4), 50)], mode="markers", marker=dict(size=13, color="red"), name="Punto actual"))
    fig4.add_vline(x=0, line_dash="dash")
    fig4.update_layout(xaxis_title="x", y
