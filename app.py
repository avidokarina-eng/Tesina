import streamlit as st
import numpy as np
import plotly.graph_objects as go
st.title("lim sin(x)/x = 1 - Tesina IA")
x = st.slider("Mover x hacia 0", -3.0, 3.0, 1.5, 0.01)
def f(v):
    return 1.0 if abs(v) < 0.0001 else np.sin(v)/v
xs = np.linspace(-3, 3, 500)
fig = go.Figure()
fig.add_trace(go.Scatter(x=xs, y=[f(i) for i in xs], name="sin(x)/x"))
fig.add_trace(go.Scatter(x=[x], y=[f(x)], mode="markers", marker=dict(size=12, color="#00cec9")))
st.plotly_chart(fig, use_container_width=True)
st.metric("f(x)", f"{f(x):.5f}")
st.metric("Error", f"{abs(f(x)-1):.5f}")
if abs(x) > 1:
    st.warning("Entrenando...")
else:
    st.success("Converge a 1 - Modelo convergido!")
