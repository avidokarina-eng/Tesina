import streamlit as st
import numpy as np
import plotly.graph_objects as go

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
    st.latex(rf"\frac{{\sin({x:.2f})}}{{{x:.2f}}} = {f(x):.5f}")

    if abs(x) > 1:
        st.warning("Entrenando...")
    else:
        st.success("Converge a 1")

elif unidad == "Unidad 1 - Límite de una función":
    st.title("Unidad 1 - Límite de una función")
    st.write("En construcción. Acá vamos a cargar la Unidad 1 luego.")
