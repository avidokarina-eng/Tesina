import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Visualizador del Limite")
st.latex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1")

x = st.slider("Mover x hacia 0", -3.0, 3.0, 1.5)

def f(v):
    return 1.0 if abs(v) < 0.0001 else np.sin(v)/v

xs = np.linspace(-3, 3, 500)
fig = go.Figure()
fig.add_trace(go.Scatter(x=xs, y=[f(i) for i in xs], mode="lines", name="f(x)"))
fig.add_trace(go.Scatter(x=[x], y=[f(x)], mode="markers", marker=dict(size=12), name="x actual"))
fig.add_hline(y=1, line_dash="dash")
st.plotly_chart(fig, use_container_width=True)

st.metric("f(x)", f"{f(x):.5f}")
st.latex(rf"\frac{{\sin({x:.2f})}}{{{x:.2f}}} = {f(x):.5f}")

if abs(x) > 1:
    st.warning("Entrenando...")
else:
    st.success("Converge a 1")
