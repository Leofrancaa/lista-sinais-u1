import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 11)  # Valores de 0 a 10
x = np.exp(1j * n)     # Calcula e^(j*n)

# Configuração do gráfico
plt.figure(figsize=(10, 6))

# Parte Real
plt.subplot(2, 1, 1)
plt.stem(n, x.real, basefmt=" ", label='Real')
plt.ylabel('Re{x[n]}')
plt.title('Partes Real e Imaginária de $x[n] = e^{j n}$')
plt.grid(True)
plt.legend()

# Parte Imaginária
plt.subplot(2, 1, 2)
plt.stem(n, x.imag, basefmt=" ", label='Imaginário', linefmt='orange')
plt.ylabel('Im{x[n]}')
plt.xlabel('n')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
plt.plot(x.real, x.imag, 'o-', markersize=8)
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Trajetória de $x[n] = e^{j n}$ no Plano Complexo')
plt.axis('equal')  # Mantém a proporção 1:1
plt.grid(True)

# Adiciona rótulos para alguns pontos
for i in [0, 1, 2, 3, 6, 10]:
    plt.text(x[i].real, x[i].imag, f'n={i}', ha='right')

plt.show()