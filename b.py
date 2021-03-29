from numpy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# # Store Fourier SPECTRUM z with a single peak at frequency 4

# z[4] = 1.0

# #IFFT of z
# u = ifft(z)*z.size
# plt.plot(u.real,'b', u.imag, 'r')

# Create Figure
#fig = go.Figure()
fig = make_subplots(rows=2, cols=1)

# Add traces, one for each slider step
for step in np.arange(0, 128, 1):
    x = np.zeros(128)
    y = np.zeros(128)
    z = x+y*1j
    z[step] = 1.0
 #   z[step2] = 1.0*1j
    u = ifft(z)*z.size
    fig.add_trace(
        go.Scatter(
            visible=False,
            mode='markers',
            # line=dict(color="#00CED1", width=6),
            name="real",
            x=np.arange(0, 128, 1),
            y=z.real), row=1, col=1)
    fig.add_trace(
        go.Scatter(
            visible=False,
            mode='markers',
            # line=dict(color="#00CED1", width=6),
            name="imag",
            x=np.arange(0, 128, 1),
            y=z.imag), row=1, col=1)
    fig.update_layout(
        xaxis_title="frequency",
        yaxis_title="amplitude"
    )

    fig.add_trace(
        go.Scatter(
            visible=False,
            # line=dict(color="#00CED1", width=6),
            mode='lines',
            name="real",
            y=u.real
        ), row=2, col=1
    )
    fig.add_trace(
        go.Scatter(
            visible=False,
            # line=dict(color="#00CED1", width=6),
            mode='lines',
            name="imag",
            y=u.imag
        ), row=2, col=1
    )
    fig.update_xaxes(title_text="time", row=2, col=1)
    fig.update_yaxes(title_text="signal", row=2, col=1)

# Make 2nd trace visible
fig.data[2].visible = True

# Create and add slider
steps = []
for i in range(0, len(fig.data), 4):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)}]
        #              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    # Toggle i'th trace to "visible"
    step["args"][0]["visible"][i:i+4] = [True, True, True, True]
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
