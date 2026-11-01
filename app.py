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
fig.add_trace(go.Scatter(x=[x], y=[f(x)], mode="markers", marker=dict(size=12), name="Punto actual"))
fig.add_hline(y=1, line_dash="dash")
st.plotly_chart(fig, use_container_width=True)

st.metric("f(x)", f"{f(x):.5f}")
st.latex(rf"\frac{{\sin({x:.2f})}}{{{x:.2f}}} = {f(x):.5f}")

if abs(x) > 1:
    st.warning("Entrenando...")
else:
    st.success("Converge a 1")

st.divider()
st.markdown("""
### Límite trigonométrico notable

Este es uno de los límites fundamentales del cálculo diferencial. Establece que, cuando el valor de x se aproxima cada vez más a cero, el cociente entre el seno de x y x se aproxima a 1.

$$ \\lim_{x \\to 0} \\frac{\\sin x}{x} = 1 $$

**Importante:** para que este resultado sea válido, el ángulo debe estar expresado en **radianes**.

#### 1. ¿Qué significa este límite?
Consideremos la función:
$$ f(x) = \\frac{\\sin x}{x} $$

Si reemplazamos x por valores cada vez más cercanos a cero, obtenemos:

| Valor de x | Valor de la función |
|---|---|
| 1.50 | 0.6650 |
| 1.0 | 0.8415 |
| 0.5 | 0.9588 |
| 0.1 | 0.9983 |
| 0.01 | 0.9999 |

Como ves, a medida que x se acerca a 0, f(x) se acerca a 1.

Esta es la base para probar que la derivada de sin(x) es cos(x).

---

#### 2. Fundamento Teórico

Para $0 < x < \\pi/2$: $\\sin(x) < x < \\tan(x)$

Entonces: $\\cos(x) < \\frac{\\sin(x)}{x} < 1$

Por el Teorema del Sándwich, cuando $x \\to 0$, $\\cos(x) \\to 1$, por lo tanto:

$$ \\lim_{x \\to 0} \\frac{\\sin x}{x} = 1 $$

**Importancia:** Es la base para derivar $\\sin(x)$ y para la aproximación $\\sin(x) \\approx x$ con ángulos pequeños.
""")
