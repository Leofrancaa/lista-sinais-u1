import numpy as np
import matplotlib.pyplot as plt

# Função impulso unitário δ[n]
def delta(n):
    return np.where(n == 0, 1, 0)

# Definição do intervalo de n
n = np.arange(-5, 6)  # Valores de -5 a 5 (inclusive)

# Cálculo de x[n]
x = 2 * delta(n + 2) - delta(n - 4)

# Plotagem
plt.figure(figsize=(10, 5))
plt.stem(n, x, linefmt='blue', markerfmt='bo', basefmt=" ", label=r'$x[n] = 2\delta[n+2] - \delta[n-4]$')
plt.xlabel('n', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.title('Gráfico de $x[n] = 2\delta[n+2] - \delta[n-4]$', fontsize=14)
plt.xticks(n)  # Mostra todos os valores de n no eixo
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.ylim(-2.5, 2.5)  # Ajusta a escala do eixo y
plt.show()