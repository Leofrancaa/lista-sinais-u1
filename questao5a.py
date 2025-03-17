import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

def unit_step(t):
    return np.where(t >= 0, 1, 0)

def x_t(t):
    return np.exp(t) * unit_step(-t)

def h_t(t):
    return unit_step(t)

def compute_convolution(t, x, h):
    dt = t[1] - t[0]
    y = convolve(x, h, mode='same') * dt
    return y

# Definição do tempo
t = np.linspace(-5, 5, 1000)
x = x_t(t)
h = h_t(t)
y = compute_convolution(t, x, h)

# Criando os subplots
fig, axes = plt.subplots(3, 1, figsize=(8, 10))

axes[0].plot(t, x, 'b', label='$x(t) = e^t u(-t)$')
axes[0].set_title('Sinal de Entrada $x(t)$')
axes[0].legend()
axes[0].grid()

axes[1].plot(t, h, 'r', label='$h(t) = u(t)$')
axes[1].set_title('Resposta ao Impulso $h(t)$')
axes[1].legend()
axes[1].grid()

axes[2].plot(t, y, 'g', label='$y(t) = x(t) * h(t)$')
axes[2].set_title('Resultado da Convolução $y(t)$')
axes[2].legend()
axes[2].grid()

plt.tight_layout()
plt.show()