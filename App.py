import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Limite sin(x)/x + IA", layout="wide", page_icon="🤖")

st.title("lim x→0 sin(x)/x = 1 | Tesina con IA")
st.caption("Herramienta interactiva para explicar el limite intuitivo")

col1, col2 = st.columns([1.7, 1])

with col1:
    zoom = st.slider("Zoom grafico", 0.5, 5.0, 3.0, 0.1)
    x = st.slider("Mover x hacia 0", -3.0, 3.0, 1.5, 0.01)
    
    def f(val):
        return 1.0 if abs(val) < 0.0001 else np.sin(val)/val
    
    xs = np.linspace(-zoom, zoom, 800)
    xs = xs[np.abs(xs) > 0.01]
    ys = [f(v) for v in xs]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=ys, mode='lines', name='sin(x)/x', line=dict(color='#6c5ce7', width=3)))
    fig.add_trace(go.Scatter(x=[0], y=[1], mode='markers', name='Limite L=1', marker=dict(size=18, color='white', line=dict(width=3, color='#00cec9'), symbol='circle-open')))
    fig.add_trace(go.Scatter(x=[x], y=[f(x)], mode='markers', text=[f"{f(x):.3f}"], textposition="top center", marker=dict(size=14, color='#00cec9')))
    
    fig.update_layout(height=450, margin=dict(l=20,r=20,t=20,b=20), xaxis=dict(gridcolor='#22263a'), yaxis=dict(gridcolor='#22263a', range=[0,1.4]), showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)
    
    st.info(f"x = {x:.4f} | f(x) = {f(x):.5f} | Error = {abs(f(x)-1):.5f}")

with col2:
    err = abs(f(x)-1)
    st.metric("Error |f(x)-1|", f"{err:.5f}")
    st.metric("Estabilidad IA", f"{max(0, 100*(1-err*2)):.0f}%")
    st.progress(int(max(0, 100*(1-err*2))))
    
    if abs(x) > 2:
        st.warning("🧠 Modelo sin entrenar: error alto, prediccion inestable")
    elif abs(x) > 0.8:
        st.info("⚙️ Entrenando: el error baja al acercar x a 0")
    elif abs(x) > 0.1:
        st.success(f"🎯 Fine-tuning: converge a L=1 con error {err:.4f}")
    else:
        st.balloons()
        st.success("✅ Modelo convergido: Límite = 1. f(0) no existe pero el límite sí.")
    
    st.markdown("---")
    st.markdown("> **Idea para tu tesina:** El límite es como entrenar una IA. No importa que falte el dato en x=0, importa hacia dónde tienden todas las predicciones de alrededor.")
    
    if st.button("▶️ Auto-convergencia"):
        st.write("¡Mirá como converge a 1!")
