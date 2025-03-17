import numpy as np
import matplotlib.pyplot as plt

# --------- Definição dos sinais em tempo discreto ---------

def x_discreto(n):
    """
    x[n] = δ[n] + 2δ[n-1] - δ[n-3].
    (Usada apenas para referência; aqui faremos x'[n]=x[n+2].)
    """
    val = 0
    if n == 0:
        val += 1
    if n == 1:
        val += 2
    if n == 3:
        val -= 1
    return val

def x_linha(n):
    """
    x'[n] = x[n+2] = δ[n+2] + 2δ[n+1] - δ[n-1].
    """
    val = 0
    # Se n+2 == 0 => n = -2 => x'[ -2 ] = 1
    if (n + 2) == 0:
        val += 1
    # Se n+2 == 1 => n = -1 => x'[ -1 ] = 2
    if (n + 2) == 1:
        val += 2
    # Se n+2 == 3 => n = 1 => x'[ 1 ] = -1
    if (n + 2) == 3:
        val -= 1
    return val

def h_discreto(n):
    """
    h[n] = 2δ[n+1] + 2δ[n-1].
    """
    val = 0
    # Se n+1 == 0 => n = -1 => h[-1] = 2
    if (n + 1) == 0:
        val += 2
    # Se n-1 == 0 => n = 1  => h[1] = 2
    if (n - 1) == 0:
        val += 2
    return val

def y_discreto(n):
    """
    y[n] = x'[n]*h[n] calculado analiticamente:
    y[n] = 2δ[n+3] + 4δ[n+2] + 2δ[n+1] + 2δ[n] - 2δ[n-2].
    """
    val = 0
    if n == -3:
        val += 2
    if n == -2:
        val += 4
    if n == -1:
        val += 2
    if n == 0:
        val += 2
    if n == 2:
        val -= 2
    return val

# --------- Função para plotar com subplots ---------

def plot_convolution_discreto():
    # Intervalo de n que cubra todos os índices relevantes
    n_vals = np.arange(-5, 6)

    # x'[n], h[n], y[n]
    xprime_vals = [x_linha(n) for n in n_vals]
    h_vals = [h_discreto(n) for n in n_vals]
    y_vals = [y_discreto(n) for n in n_vals]

    fig, axs = plt.subplots(3, 1, figsize=(8, 8))
    # Subplot 1: x'[n]
    axs[0].stem(n_vals, xprime_vals)
    axs[0].set_title("x'[n] = x[n+2]")
    axs[0].grid(True)

    # Subplot 2: h[n]
    axs[1].stem(n_vals, h_vals)
    axs[1].set_title("h[n]")
    axs[1].grid(True)

    # Subplot 3: y[n]
    axs[2].stem(n_vals, y_vals)
    axs[2].set_title("y[n] = x'[n] * h[n]")
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Plot da parte (b)
    plot_convolution_discreto()
