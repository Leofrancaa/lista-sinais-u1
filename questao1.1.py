import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Função degrau unitário (u(t - a))
def u(t, a):
    return np.heaviside(t - a, 1)

def f(t):
    return (3 * (u(t, 0) - u(t, 2)) - 3 * (u(t, 2) - u(t, 4)) 
            + 3 * (u(t, 4) - u(t, 6)) - 3 * (u(t, 6) - u(t, 8)))


# Gráfico Estático (Primeira Figura)

plt.figure(figsize=(12, 5))
t_static = np.linspace(-1, 9, 1000)
f_t_static = f(t_static)

# Plotagem do gráfico estático
plt.plot(t_static, f_t_static, linewidth=2, color='blue')
plt.title('Gráfico Estático')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle='--', alpha=0.5)
plt.ylim(-5, 5)

# Linhas de referência
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
for ponto in [0, 2, 4, 6, 8]:
    plt.axvline(ponto, color='red', linestyle=':', alpha=0.7)


# Animação 

fig_anim, ax_anim = plt.subplots(figsize=(12, 5))
t_anim = np.linspace(-1, 9, 1000)
f_t_anim = f(t_anim)

# Configurações da animação
ax_anim.set_title('Animação do Gráfico')
ax_anim.set_xlabel('Tempo (s)')
ax_anim.set_ylabel('Amplitude')
ax_anim.grid(True, linestyle='--', alpha=0.5)
ax_anim.set_ylim(-5, 5)
ax_anim.axhline(0, color='black', linewidth=0.8)
ax_anim.axvline(0, color='black', linewidth=0.8)
for ponto in [0, 2, 4, 6, 8]:
    ax_anim.axvline(ponto, color='red', linestyle=':', alpha=0.7)

# Objeto para a linha animada
line, = ax_anim.plot([], [], lw=2, color='blue')

# Funções de inicialização e animação
def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(t_anim[:i], f_t_anim[:i])
    return line,

# Cria a animação
anim = FuncAnimation(
    fig_anim, animate, init_func=init,
    frames=len(t_anim), interval=2, blit=True
)

# Exibe ambas as figuras
plt.show()