import numpy as np
import matplotlib.pyplot as plt

# Função degrau unitário (u(t - a))
def u(t, a):
    return np.heaviside(t - a, 1)

# Parâmetros
T = 6  # período total em segundos
amplitude_max = 3  # amplitude máxima (calculada com base na inclinação)

# Função da onda triangular
def f(t):
    termo1 = (t + T/2) * u(t, -T/2)  # (t + 3)u(t + 3)
    termo2 = -2 * t * u(t, 0)        # -2t u(t)
    termo3 = (t - T/2) * u(t, T/2)   # (t - 3)u(t - 3)
    return termo1 + termo2 + termo3

# Vetor de tempo simétrico (de -5 a 5 segundos)
t = np.linspace(-5, 5, 1000)

# Cálculo da onda triangular
f_t = f(t)

# Plotagem do gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, f_t, linewidth=2, color='purple')
plt.title('Onda Triangular Simétrica Modelada por Funções Degrau')
plt.xlabel('Tempo (s)')
plt.ylabel('f(t)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-0.5, amplitude_max + 0.5)
plt.xlim(-5, 5)

# Destacar os pontos de transição
plt.axvline(-T/2, color='red', linestyle='--', alpha=0.5, label='-T/2')
plt.axvline(T/2, color='green', linestyle='--', alpha=0.5, label='T/2')
plt.axvline(0, color='black', linestyle='--', alpha=0.5)
plt.legend()

plt.show()