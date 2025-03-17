import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
A = 6
T = 3  # segundos

# Função degrau unitário (u(t - a))
def u(t, a):
    return np.heaviside(t - a, 1)

# Vetor de tempo simétrico (de -5 a 5 segundos)
t = np.linspace(-5, 5, 1000)

# Cálculo do pulso retangular
i_t = A * (u(t, -T/2) - u(t, T/2))

# Plotagem do gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, i_t, linewidth=2, color='blue')
plt.title('Pulso Retangular Simétrico Modelado por Funções Degrau')
plt.xlabel('Tempo (s)')
plt.ylabel('i(t)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-0.5, A + 0.5)
plt.xlim(-5, 5)

# Destacar os pontos de transição
plt.axvline(-T/2, color='red', linestyle='--', alpha=0.5, label='-T/2')
plt.axvline(T/2, color='green', linestyle='--', alpha=0.5, label='T/2')
plt.legend()

plt.show()