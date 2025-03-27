import numpy as np
import matplotlib.pyplot as plt

# Função degrau unitário (u(t - a))
def u(t, a):
    return np.heaviside(t - a, 1)


def f(t):
    return (3 * (u(t, 0) - u(t, 2)) - 3 * (u(t, 2) - u(t, 4)) + 3 * (u(t, 4) - u(t, 6)) - 3 * (u(t, 6) - u(t, 8)))

# Vetor de tempo (de -1 a 9 segundos)
t = np.linspace(-1, 9, 1000)
f_t = f(t)

# Plotagem do gráfico
plt.figure(figsize=(12, 5))
plt.plot(t, f_t, linewidth=2, color='blue')
plt.title('Gráfico da Função')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle='--', alpha=0.5)
plt.ylim(-5, 5)

# Linhas de referência e transições
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
for ponto in [0, 2, 4, 6, 8]:
    plt.axvline(ponto, color='red', linestyle=':', alpha=0.7)

plt.show()