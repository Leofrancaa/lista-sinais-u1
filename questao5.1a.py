import numpy as np
import matplotlib.pyplot as plt

# Funções originais
def x(t):
    return np.exp(t) * (t <= 0)  # x(t) = e^t u(-t)

def h(t):
    return (t >= 0).astype(float)  # h(t) = u(t)

# Discretização do tempo
t = np.linspace(-5, 5, 1000)
dt = t[1] - t[0]

# Cálculo da convolução
y_conv = np.convolve(x(t), h(t), mode='same') * dt

# Plotagem com subplots
plt.figure(figsize=(10, 8))

# Subplot 1: x(t)
plt.subplot(3, 1, 1)
plt.plot(t, x(t), color='blue', label='$x(t) = e^t u(-t)$')
plt.title('Sinais Originais e Convolução Contínua')
plt.ylabel('$x(t)$')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Subplot 2: h(t)
plt.subplot(3, 1, 2)
plt.plot(t, h(t), color='orange', label='$h(t) = u(t)$')
plt.ylabel('$h(t)$')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Subplot 3: Convolução
plt.subplot(3, 1, 3)
plt.plot(t, y_conv, color='green', label='$y(t) = x(t) * h(t)$')
plt.xlabel('$t$')
plt.ylabel('$y(t)$')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.tight_layout()
plt.show()