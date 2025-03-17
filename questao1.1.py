import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
A = 3
T = 2  # segundos

# Função degrau unitário (u(t - a))
def u(t, a):
    return np.heaviside(t - a, 1)

# Função da forma de onda quadrada como soma de degraus
def v(t, num_termos=5):
    soma = A * u(t, 0)  # Primeiro termo: A*u(t)
    sinal = -1  # Alternância de sinais nos termos seguintes
    for n in range(1, num_termos):
        a = (2*n - 1) * T  # Pontos de transição: T, 3T, 5T, ...
        soma += (2 * A * sinal) * u(t, a)
        sinal *= -1  # Inverte o sinal para o próximo termo
    return soma

# Geração do vetor de tempo (de 0 a 10 segundos)
t = np.linspace(0, 10, 1000)

# Cálculo da forma de onda
num_termos = 5  # Número de termos na série (ajuste conforme necessário)
v_t = v(t, num_termos)

# Plotagem do gráfico
plt.figure(figsize=(10, 4))
plt.plot(t, v_t, linewidth=2)
plt.title('Forma de Onda Quadrada Modelada por Funções Degrau')
plt.xlabel('Tempo (s)')
plt.ylabel('v(t)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.ylim(-A*1.2, A*1.2)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Destacar os pontos de transição (T, 3T, 5T...)
for n in range(1, num_termos + 1):
    transicao = (2*n - 1) * T
    plt.axvline(transicao, color='red', linestyle='--', alpha=0.5)

plt.show()