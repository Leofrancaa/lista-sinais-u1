import numpy as np
import matplotlib.pyplot as plt

# Definir as sequências
def x_shifted(n):
    return (n == -2) + 2*(n == -1) - (n == 1)  # x[n+2] = δ[n+2] + 2δ[n+1] - δ[n-1]

def h_n(n):
    return 2*(n == -1) + 2*(n == 1)  # h[n] = 2δ[n+1] + 2δ[n-1]

# Índices e valores
n_x = np.array([-2, -1, 1])
x_values = np.array([1, 2, -1])

n_h = np.array([-1, 1])
h_values = np.array([2, 2])

n_result = np.array([-3, -2, -1, 0, 2])
y_values = np.array([2, 4, 2, 2, -2])

# Plotagem com subplots
plt.figure(figsize=(10, 8))

# Subplot 1: x[n+2]
plt.subplot(3, 1, 1)
plt.stem(n_x, x_values, linefmt='b-', markerfmt='bo', basefmt=' ', label='$x[n+2]$')
plt.title('Sinais Originais e Convolução Discreta')
plt.ylabel('$x[n+2]$')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(np.arange(-3, 3))
plt.legend()

# Subplot 2: h[n]
plt.subplot(3, 1, 2)
plt.stem(n_h, h_values, linefmt='r-', markerfmt='ro', basefmt=' ', label='$h[n]$')
plt.ylabel('$h[n]$')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(np.arange(-3, 3))
plt.legend()

# Subplot 3: y[n]
plt.subplot(3, 1, 3)
plt.stem(n_result, y_values, linefmt='g-', markerfmt='go', basefmt=' ', label='$y[n] = x[n+2] * h[n]$')
plt.xlabel('$n$')
plt.ylabel('$y[n]$')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(np.arange(-3, 3))
plt.legend()

plt.tight_layout()
plt.show()

