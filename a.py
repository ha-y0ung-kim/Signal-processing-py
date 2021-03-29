''' Python script to demonstrate Fourier synthesis '''
from numpy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import math

# .. initialize complex array to store Fourier coefficients
x = np.zeros(128)
y = np.zeros(128)
z = x+y*1j
# .. uncomment one line to set Fourier coefficients

init_x = 1
init_y = 0
init_k = 4


def f(x, y, k):
    z[k] = x + y * 1j
    return z


#z[4]=1; addstr = 'z[4]=1'
# z[4] = 1j
# addstr = 'z[4]=i'
# ---z[4]=1+1j; addstr = 'z[4]=1+i'
# ---z[125]=1; addstr = 'z[125]=1'
#z[21]=z[22]=0.5; addstr = 'z[21]=z[22]=0.5'
# ---z[4]=(1+1j)/np.sqrt(8); z[124]=(1-1j)/np.sqrt(8); addstr='cos_phi=45'
# .. Fourier synthesis = inverse Fourier transform

u = ifft(z)*math.sqrt(z.size)


def g(z):
    u = ifft(z)*math.sqrt(z.size)
    return u


# .. plot Fourier coefficients and synthesized signal


# # plt.title('Harmonic signal for '+addstr)
# #---plt.title('Cosine signal, phase shift $\pi/4$')
# plt.xlabel('Time [s]')
# plt.ylabel('Signal [arb. units]')
# plt.legend(loc=4)
# .. save figure in png format
# plt.savefig('DemoFourierSynthesis_'+addstr+'.png',frameon=False,bbox_inches='tight')
# plt.close()


fig, ax = plt.subplots()
plt.subplot(2, 1, 1)
line1, = plt.plot(z.real, 'b', label='Real part')
line2, = plt.plot(z.imag, 'r', label='Imaginary part')
plt.xlim(0, 128)
plt.ylim(0, 10)


plt.subplot(2, 1, 2)
line3, = plt.plot(u.real, 'b', label='Real part')
line4, = plt.plot(u.imag, 'r', label='Imaginary part')
plt.xlim(0, z.size)
plt.ylim(-1, 1)
 
ax.set_xlabel('Time [s]')


axcolor = 'lightgoldenrodyellow'
ax.margins(x=0)

# adjust the main plot to make room for the sliders
plt.subplots_adjust(left=0.25, bottom=0.5)

# Make a horizontal slider to control the real value.
axfreq = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
real_slider = Slider(
    ax=axfreq,
    label='real',
    valstep=0.5,
    valmin=0,
    valmax=10,
    valinit=init_x,
)

# Make a vertically oriented slider to control the imag value
axamp = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
imag_slider = Slider(
    ax=axamp,
    label="imag",
    valmin=0,
    valstep=0.5,
    valinit=init_y,
    valmax=10
    # orientation="vertical"
)

axz = plt.axes([0.25, 0.3, 0.65, 0.03], facecolor=axcolor)
z_slider = Slider(
    ax=axz,
    label="z",
    valmin=0,
    valstep=1,
    valinit=init_k,
    valmax=100
    # orientation="vertical"
)


# The function to be called anytime a slider's value changes
def update(val):
    z = f(real_slider.val, imag_slider.val, z_slider.val)
    line1.set_ydata(z.real)
    line2.set_ydata(z.imag)
    line3.set_ydata(g(z).real)
    line4.set_ydata(g(z).imag)
    fig.canvas.draw_idle()


# register the update function with each slider
real_slider.on_changed(update)
imag_slider.on_changed(update)
z_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    real_slider.reset()
    imag_slider.reset()
    z_slider.val.reset()


button.on_clicked(reset)


plt.show()
