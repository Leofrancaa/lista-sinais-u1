import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 11)  # Valores de 0 a 10 (inteiros)

# Componentes individuais
cosseno = 2 * np.cos(0.1 * np.pi * n + np.pi/3)
seno = 2 * np.sin(0.5 * np.pi * n)

plt.figure(figsize=(12, 6))

# Componente do cosseno
plt.subplot(2, 1, 1)
plt.stem(n, cosseno, linefmt='red', markerfmt='ro', basefmt=" ")
plt.title('$2\cos(0.1\pi n + \pi/3)$')
plt.grid(True)

# Componente do seno
plt.subplot(2, 1, 2)
plt.stem(n, seno, linefmt='green', markerfmt='go', basefmt=" ")
plt.title('$2\sin(0.5\pi n)$')
plt.xlabel('n')
plt.grid(True)

plt.tight_layout()
plt.show()



# Calcula x[n] = 2cos(0.1πn + π/3) + 2sen(0.5πn)
x = 2 * np.cos(0.1 * np.pi * n + np.pi/3) + 2 * np.sin(0.5 * np.pi * n)

# Configuração do gráfico
plt.figure(figsize=(10, 5))
plt.stem(n, x, linefmt='blue', markerfmt='o', basefmt=" ", label='$x[n]$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Gráfico de $x[n] = 2\cos(0.1\pi n + \pi/3) + 2\sin(0.5\pi n)$')
plt.grid(True)
plt.legend()
plt.xticks(n)  # Mostra todos os valores de n no eixo x
plt.show()

