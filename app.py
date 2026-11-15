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
