from numpy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import math

t = np.arange(0, 3, 0.001)  # time [s]


def summ(t, n):
    r = np.zeros(t.size)
    for i in range(n):
        r += np.sin((2*i-1)*np.pi*t)/(2*i-1)
    return 4*r/np.pi


# Create Figure
fig = go.Figure()

# Add traces, one for each slider step
for step in np.arange(1, 200, 1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            mode='lines',
            # line=dict(color="#00CED1", width=6),
            name="real",
            x=t,
            y=summ(t, step)))
    fig.update_layout(
        xaxis_title="time"
    )
# Make 2nd trace visible
fig.data[0].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)}]
        #              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    # Toggle i'th trace to "visible"
    step["args"][0]["visible"][i] = [True]
    steps.append(step)


sliders = [dict(
    active=0,
    pad={"t": 50},
    steps=steps
)]


fig.update_layout(
    sliders=sliders,
)

fig.show()
# fig.write_html("../booya/a.html")
