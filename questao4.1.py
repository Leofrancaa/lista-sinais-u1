import numpy as np
import matplotlib.pyplot as plt

# Função degrau unitário (u(t - a))
def u(t, a):
    return np.heaviside(t - a, 1)

# Vetor de tempo (de 0 a 4 segundos)
t = np.linspace(-1, 4, 1000)

# Cálculo da forma de onda
v_t = 1 * u(t, 0) + 1 * u(t, 1) + 1 * u(t, 2) - 3 * u(t, 3)

# Plotagem do gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, v_t, linewidth=2, color='darkorange')
plt.title('Forma de Onda com Degraus Sucessivos e Reset')
plt.xlabel('Tempo (s)')
plt.ylabel('v(t)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-0.5, 3.5)
plt.xlim(-0.5, 4)

# Destacar os pontos de transição
for transition in [0, 1, 2, 3]:
    plt.axvline(transition, color='red', linestyle='--', alpha=0.5)

plt.show()