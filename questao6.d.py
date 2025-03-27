import numpy as np
import matplotlib.pyplot as plt

# Função degrau unitário u[n]
def u(n):
    return np.where(n >= 0, 1, 0)

# Intervalo de n (0 a 20)
n = np.arange(0, 21)

# Cálculo das componentes
part1 = n * (u(n) - u(n - 10))            # Primeira parte: n*(u[n] - u[n-10])
part2 = (10 - 0.3*(n - 10)) * (u(n - 10) - u(n - 20))  # Segunda parte: (10-0.3(n-10))*(u[n-10] - u[n-20])
x = part1 + part2                          # Soma das componentes

# Plotagem
plt.figure(figsize=(12, 6))
plt.stem(n, x, linefmt='blue', markerfmt='bo', basefmt=" ", label='$x[n]$')
plt.xlabel('$n$', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.title('$x[n] = n[u[n]−u[n−10]] + (10−0.3(n−10))[u[n−10] − u[n−20]]$', fontsize=14)
plt.xticks(np.arange(0, 21, 2))  # Marcadores de n de 0 a 20, passo 2
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(-1, 11)  # Ajuste do eixo y
plt.legend()
plt.show()