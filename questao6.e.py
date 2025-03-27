import numpy as np
import matplotlib.pyplot as plt

# Função impulso unitário δ[n]
def delta(n, k):
    return np.where(n == k, 1, 0)

# Intervalo de n (0 a 25)
n = np.arange(0, 26)

# Inicializa x[n] com zeros
x = np.zeros_like(n, dtype=float)

# Calcula a soma para cada m de 0 a 10
for m in range(0, 11):
    amplitude = m + 1
    x += amplitude * (delta(n, 2*m) - delta(n, 2*m + 1))

# Plotagem
plt.figure(figsize=(14, 6))
plt.stem(n, x, linefmt='blue', markerfmt='bo', basefmt=" ", label=r'$x[n]$')
plt.xlabel('$n$', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.title(r'$x[n] = \sum_{m=0}^{10} (m+1)[\delta(n-2m) - \delta(n-2m-1)]$', fontsize=14)
plt.xticks(np.arange(0, 26, 2))  # Marcadores de n a cada 2 unidades
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(-12, 12)  # Ajuste do eixo y para incluir amplitudes até ±11
plt.legend()
plt.show()